import subprocess
import threading
import re
import uuid

class run_command:
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
        self.output = []
        self.last_index = 0
        self._start_reading()

    def _start_reading(self):
        def read_output(pipe, output_list):
            for line in iter(pipe.readline, ''):
                output_list.append(line.strip())
            pipe.close()

        self.stdout_thread = threading.Thread(target=read_output, args=(self.process.stdout, self.output))
        self.stderr_thread = threading.Thread(target=read_output, args=(self.process.stderr, self.output))
        
        self.stdout_thread.start()
        self.stderr_thread.start()

    def get_part(self):
        current_output = self.output[self.last_index:]
        self.last_index = len(self.output)
        return "\n".join(current_output)

    def get_con(self):
        return self.process.poll() is not None

    def get_all(self):
        return "\n".join(self.output)

class modern_replace:
    def dict_replace(text,replacements,regex=False):
        if regex:
            for old, new in replacements.items():
                text = re.sub(old, new, text)
            return text
        else:
            for old, new in replacements.items():
                text = text.replace(old, new)
            return text

    def cross_replace(text, a, b):
        while True:
            temp = str(uuid.uuid4())
            if temp not in text:
                break
        return text.replace(a, temp).replace(b, a).replace(temp, b)
    
    def count_replace(text,a,b,count=-1):
        if count == -1:
            while a in text:
                text = text.replace(a,b)
        elif count < -1:
            return ""
        else:
            for i in range(count):
                text = text.replace(a,b)
        return text

class modern_str:
    def add_text(text,text_len,add_str=" "):
        if len(text) >= text_len:
            return text
        remaining_length = text_len - len(text)
        new_text = text + (add_str * (remaining_length // len(add_str))) + add_str[:remaining_length % len(add_str)]
        return new_text