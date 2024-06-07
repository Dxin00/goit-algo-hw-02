import queue
import random
import time

class ServiceCenter:
    def __init__(self):
        self.request_queue = queue.Queue()

    def generate_request(self):
        request_id = random.randint(1000, 9999)
        print(f"Нова заявка додана: {request_id}")
        self.request_queue.put(request_id)

    def process_request(self):
        if not self.request_queue.empty():
            request_id = self.request_queue.get()
            print(f"Обробка заявки: {request_id}")
            time.sleep(1)
        else:
            print("Черга пуста, нема заявок для обробки.")

    def view_requests(self):
        if not self.request_queue.empty():
            print("Заявки в черзі:")
            temp_list = []
            while not self.request_queue.empty():
                request_id = self.request_queue.get()
                print(request_id)
                temp_list.append(request_id)
            for request_id in temp_list:
                self.request_queue.put(request_id)
        else:
            print("Черга пуста.")

def main():
    service_center = ServiceCenter()
    
    try:
        while True:
            action = input("Введіть 'n' для нової заявки, 'p' для обробки заявки, 'v' для перегляду черги, або 'q' для виходу: ").strip().lower()
            if action == 'n':
                service_center.generate_request()
            elif action == 'p':
                service_center.process_request()
            elif action == 'v':
                service_center.view_requests()
            elif action == 'q':
                print("Завершення програми.")
                break
            else:
                print("Неправильна команда. Спробуйте знову.")
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == "__main__":
    main()
