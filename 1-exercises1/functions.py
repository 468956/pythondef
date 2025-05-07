from datetime import date

# 1. 💰 Calculadora de propina  

def calculate_tip(amount, tip):
    totalTip = amount*(tip/100)
    return totalTip

#print(calculate_tip(100, 15))

# 2. 📏 Conversor de unidades  

def meters_to_kilometers(m):
    resultKm = m/1000
    return resultKm

print(meters_to_kilometers(1500))

# 3. ✉️ Generador de email empresarial 

def create_email(name, lastname, domain):
    return f"{name.lower()}.{lastname.lower()}@{domain.lower()}"

print(create_email("Lucia", "Gomez", "empresa"))

# 4. 🧾 Precio con impuestos  

def final_price(base_price, iva=0.21):
    return base_price + (base_price*iva)

print(final_price(100, 0.10))
print(final_price(100))

# 5. 🔐 Simulador de login  

def validate_login(user, password):
    if user == "admin":
        print("Inicio de sesión exitoso")
        return True
    else:
        print ("Credenciales incorrectas")
        return False

validate_login("admin", "1234")
validate_login("user", "wrong")

# 6. 🧑‍💻 Generador de nombre de usuario  

def generate_username(name, birth):
    return  f"{name.lower()}{date(birth, 1, 1).strftime("%y")}"


print(generate_username("Lucas", 1992))

# 7. ✨ Formateador de nombres  

def format_name(full_name):
    return full_name.title()
print(format_name("juan perez"))

# 8. 🎂 Calculadora de edad  

def calculate_age(year_of_birth):
    return date.today().year - year_of_birth

print(calculate_age(1998))

# 9. 📞 Validación de número telefónico  

def validate_phone(number):
    if not len(str(number)) == 10:
        return False
    elif type(number) is str:
        return False
    else:
        return True

    #return True if len(number) == 10 else False


print(validate_phone(1234567890))
print(validate_phone(1234))
print(validate_phone("abcdefghij"))

# 10. 🧠 Notas de estudiantes  

def student_average(name, grade1, grade2, grade3):
    return print(f"{name}: Promedio = {(grade1+grade2+grade3)/3:.2f}")

print(student_average("Ana", 8, 9, 7))
