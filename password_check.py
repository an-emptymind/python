print("----Welcome to Password strength checker----")
password= input("Enter your password")

capitals=[w for w in password if w.isupper()]
#print(f"Capitals:",capitals)

smalls=[l for l in password if l.islower()]
#print("Smalls:",smalls)

digits=[d for d in password if d.isdigit()]
#print("Digits:",digits)

specials=[s for s in password if not s.isalnum()]
#print("Specials:",specials)

print(f"Length: {len(password)} | Capitals: {len(capitals)} | smalls: {len(smalls)} | digits: {len(digits)} | specials: {len(specials)}")

if len(password) <8:
    print("Password length should be grater than 8.")
elif len(capitals) == 0:
    print("Atlest 1 capital letter required")
elif len(smalls) == 0:
    print("Atleast 1 small letter required")
elif len(digits) == 0:
    print("Atleast 1 numerical value required")
elif len(specials) == 0:
    print("Atleast 1 special character required")
else:
    print("Valid password")

