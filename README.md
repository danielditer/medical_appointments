To initialize this project:
```sh
git clone https://github.com/danielditer/medical_appointments.git
cd medical_appointments/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

To run this project:
```sh
python manage.py runserver
```

Admin user credentials: 
```sh
admin/admin
```

Request example:
```sh
http://127.0.0.1:8000/api/prescriptions/filter-by-patient-first-name/Jane
```
```json
[
    {
        "id": 2,
        "appointment": {
            "doctor": {
                "first_name": "Bob",
                "last_name": "Green",
                "specialty": "Medicina General"
            },
            "date": "2024-08-01",
            "time": "11:00:00"
        },
        "medication": "Ibuprofeno",
        "dosage": 200
    },
    {
        "id": 3,
        "appointment": {
            "doctor": {
                "first_name": "Alice",
                "last_name": "Brown",
                "specialty": "Pediatria"
            },
            "date": "2024-07-28",
            "time": "23:22:41"
        },
        "medication": "Paracetamol",
        "dosage": 10
    }
]
```