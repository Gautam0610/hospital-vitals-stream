
import random
import time
import json


def generate_vitals():
    patient_id = random.randint(1000, 9999)
    heart_rate = random.randint(60, 100)
    breaths_per_minute = random.randint(12, 20)
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    blood_pressure_systolic = random.randint(110, 130)
    blood_pressure_diastolic = random.randint(70, 90)
    oxygen_saturation = random.randint(95, 99)

    # Simulate occasional unrealistic values
    if random.random() < 0.01:  # 1% chance
        heart_rate = random.randint(150, 220)  # Extremely high
    elif random.random() < 0.02:
        heart_rate = random.randint(30, 50)  # Extremely low

    if random.random() < 0.01:
        breaths_per_minute = random.randint(30, 50)  # Extremely high
    elif random.random() < 0.02:
        breaths_per_minute = random.randint(5, 10)  # Extremely low

    vitals = {
        "patient_id": patient_id,
        "heart_rate": heart_rate,
        "breaths_per_minute": breaths_per_minute,
        "body_temperature": body_temperature,
        "blood_pressure_systolic": blood_pressure_systolic,
        "blood_pressure_diastolic": blood_pressure_diastolic,
        "oxygen_saturation": oxygen_saturation
    }
    return vitals


if __name__ == '__main__':
    while True:
        vitals_data = generate_vitals()
        print(json.dumps(vitals_data))
        time.sleep(1)  # Send data every 1 second
