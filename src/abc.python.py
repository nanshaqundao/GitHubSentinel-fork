import csv
import random
from datetime import datetime, timedelta


def generate_content(index):
    content_types = [
        f"Technical review for product variant {index}",
        f"Customer feedback analysis report {index}",
        f"Quality assurance testing results {index}",
        f"Market research findings document {index}",
        f"Production specification details {index}"
    ]
    base_content = random.choice(content_types)
    return base_content + " " + "x" * random.randint(100, 500)


def generate_data():
    with open('business_order_payload.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'order_number', 'content'])

        for i in range(10000):
            name = "TimeMachine"
            order_number = f"ORD-{i:05d}"
            content = generate_content(i)
            writer.writerow([name, order_number, content])


if __name__ == "__main__":
    generate_data()