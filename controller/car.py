cars = {
    1: {'id': 1, 'plate': 'abc1234', 'brand': 'bmw', 'model': 'x6', 'color': 'branca', 'manufacturing_date': '2024'}
}


class CarController:
    def create(self, plate, brand, model, color, manufacturing_date):
        plate_exists = self.exists_with_this_plate(plate)

        if not plate_exists:
            id = max(cars.keys()) + 1 if cars else 1

            cars[id] = dict(
                id=id,
                plate=plate,
                brand=brand,
                model=model,
                color=color,
                manufacturing_date=manufacturing_date
            )

            return cars, True

        return None, False

    def list(self):
        return [car for _, car in cars.items()]

    def get_by_id(self, id):
        return cars.get(id)

    def update(self, id, plate, brand, model, color, manufacturing_date):
        plate_exists = self.exists_with_this_plate(plate)

        if not plate_exists:
            cars[id] = dict(
                id=id,
                plate=plate,
                brand=brand,
                model=model,
                color=color,
                manufacturing_date=manufacturing_date
            )

            return cars, True
        else:
            return None, False

    def delete(self, id):
        del cars[id]

    def exists_with_this_plate(self, plate: str) -> bool:
        for _, car in cars.items():
            if car['plate'] == plate:
                return True

        return False

    def exists_with_this_id(self, car_id: int) -> bool:
        return self.get_by_id(car_id) is not None
