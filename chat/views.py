from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
import subprocess

def index(request):
    return render(request, 'index.html')

def stream_with_ollama(prompt):
    process = subprocess.Popen(
        ['wsl', '-u', 'gajendra', '--exec', 'ollama', 'run', 'gemma:2b', prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # Force line buffering
    )

    def stream():
        empty_count = 0  # Track consecutive empty reads
        answer = ""  # Collect the full response

        while True:
            char = process.stdout.read(1)  # Read one character at a time
            poll_result = process.poll()  # Check if process has finished

            if char == "":  # If empty, count consecutive occurrences
                empty_count += 1
            else:
                empty_count = 0  # Reset if valid character received
                answer += char  # Append character to answer

            # If process is done & we received empty characters multiple times, exit
            if empty_count >= 2 and poll_result is not None:
                print("Process finished with return code:", poll_result)
                break

            if char:  # Send only non-empty characters
                yield f"data: {char}\n\n"

        # Ensure the process is fully closed
        process.stdout.close()
        process.wait()

        if process.returncode != 0:  # Handle errors
            stderr = process.stderr.read().strip()
            yield f"data: Error: {stderr}\n\n"

        # Print the full response after the process finishes
        print("Answer:", answer.strip())

        # End of streaming signal
        yield "data: [END]\n\n"

    return iter(stream())  # Convert generator function to an iterable

def chat(request):
    if request.method == 'GET':
        prompt = request.GET.get('prompt', '')
        print("Prompt:", prompt)
        if not prompt:
            return HttpResponse("Prompt is required", status=400)

        response = StreamingHttpResponse(stream_with_ollama(prompt), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        response['X-Accel-Buffering'] = 'no'  # Prevent buffering by reverse proxies
        return response

    return HttpResponse("Invalid method", status=405)
