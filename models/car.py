import csv

class Car:
    def __init__(self):
        self.filename = 'car.csv'
        self.fieldnames = ['id', 'plate', 'brand', 'model', 'color', 'manufacturing_date']

    def create(self, plate, brand, model, color, manufacturing_date):
        cars = self.list()
        is_empty = len(cars) == 0

        if is_empty:
            car_id = 1

        else:
            last_account_id = cars[-1].get('id')
            car_id = int(last_account_id) + 1

        if not self.exists_with_this_plate(plate):
            car = dict(
                id=car_id,
                plate=plate,
                brand=brand,
                model=model,
                color=color,
                manufacturing_date=manufacturing_date
            )
            with open(self.filename, 'a+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

                if is_empty:
                    writer.writeheader()

                writer.writerow(car)

            return car, True

        else:
            return None, False

    def update(self, id, plate, brand, model, color, manufacturing_date):
        cars = self.list()
        car_found = False

        for car in cars:
            if car['id'] == str(id):
                car_found = True
                car['plate'] = plate
                car['brand'] = brand
                car['model'] = model
                car['color'] = color
                car['manufacturing_date'] = manufacturing_date
                break

        if not car_found:
            return None, False

        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(cars)

        return cars, True

    def list(self):
        data = []

        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)

        return data

    def get_by_id(self, id):
        cars = self.list()
        for car in cars:
            if car['id'] == str(id):
                return car
        return None

    def delete(self, id):
        car_exists = self.get_by_id(id)

        if car_exists:
            cars = self.list()

            for car in cars:
                if car['id'] == str(id):
                    cars.remove(car)
                    break

            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(cars)

            return True
        else:
            return False

    def exists_with_this_plate(self, plate):
        cars = self.list()
        for car in cars:
            if car['plate'] == plate:
                return True
        return False

    def exists_with_this_id(self, car_id: int) -> bool:
        return self.get_by_id(car_id) is not None
