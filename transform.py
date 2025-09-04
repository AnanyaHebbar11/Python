import pandas as pd

def transform_data(cd):
    new_cd = cd.copy()

    # Clean names
    new_cd['name'] = new_cd['name'].str.replace(" ", "", regex=False).str.lower()

    # Clean phone numbers (keep only digits, fill missing, keep last 10 digits, add +1 prefix)
    new_cd['phone'] = new_cd['phone'].replace(r'[^0-9]', '', regex=True)
    new_cd['phone'] = new_cd['phone'].fillna("9999999999")
    new_cd['phone'] = new_cd['phone'].str[-10:]
    new_cd['phone'] = '+1' + new_cd['phone']

    # Clean email
    new_cd['email'] = new_cd['email'].str.strip().str.lower()
    new_cd['email'] = new_cd['email'].fillna(new_cd['name'] + "@example.com")

    # Parse registration_date safely
    new_cd["registration_date"] = pd.to_datetime(
        new_cd["registration_date"],
        errors="coerce",          # Invalid → NaT
        dayfirst=True             # ✅ set according to your data (change to False if MM-DD-YYYY)
    )

    # Fill missing registration dates with a default
    new_cd["registration_date"] = new_cd["registration_date"].fillna(
        pd.Timestamp("2003-03-23")
    )

    return new_cd
