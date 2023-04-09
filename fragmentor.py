
import pandas as pd

df = pd.read_excel('Cars.xlsx')

new_rows = []
for _, row in df.iterrows():
    code = row['Code']
    persian_name = row['PersianName']
    if type(row['CarModels']) == str:
        carModels = row['CarModels'].split(',')
        print(carModels)
        for car_model in carModels:
            new_rows.append({'Code': code, 'PersianName': persian_name, 'CarModel': car_model})
    else:
        new_rows.append({'Code': code, 'PersianName': persian_name, 'CarModel': ''})

new_df = pd.DataFrame(new_rows)

# Save the new DataFrame to a new Excel file
new_df.to_excel('new_cars.xlsx', index=False)
