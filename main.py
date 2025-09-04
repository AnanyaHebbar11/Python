import extract
import transform
import load

raw_data=extract.read_data()

new_cd=transform.transform_data(raw_data)

status = load.insert_data(new_cd, "c")

print(status)

   

