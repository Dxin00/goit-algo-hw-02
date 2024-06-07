import queue
import random
import time

class ServiceCenter:
    def __init__(self):
        self.request_queue = queue.Queue()

    def generate_request(self):
        request_id = random.randint(1000, 9999)
        print(f"Новая заявка добавлена: {request_id}")
        self.request_queue.put(request_id)

    def process_request(self):
        if not self.request_queue.empty():
            request_id = self.request_queue.get()
            print(f"Обработка заявки: {request_id}")
            time.sleep(1)
        else:
            print("Очередь пуста, нет заявок для обработки.")

def main():
    service_center = ServiceCenter()
    
    try:
        while True:
            action = input("Введите 'n' для новой заявки, 'p' для обработки заявки, или 'q' для выхода: ").strip().lower()
            if action == 'n':
                service_center.generate_request()
            elif action == 'p':
                service_center.process_request()
            elif action == 'q':
                print("Завершение программы.")
                break
            else:
                print("Неверная команда. Попробуйте снова.")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")

if __name__ == "__main__":
    main()
