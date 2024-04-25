import pandas as pd
import numpy as np
from PIL import Image
import sqlite3

# Load the CSV file
df = pd.read_csv('Challenge2.csv')
df = df.dropna()

# The first column is 'depth' and the rest are pixel values
depths = df['depth'].values  # This stores the depth values if needed
image = df.drop('depth', axis=1).values  # This drops the depth column and keeps only pixel values

# Convert numpy array to PIL Image
image_pil = Image.fromarray(image.astype(np.uint8))

# Resize the image
new_width = 150
new_height = image_pil.height  # Keeping the original height the same
resized_image_pil = image_pil.resize((new_width, new_height))
# Convert back to numpy array 
resized_image = np.array(resized_image_pil)

# Create DataFrame
df_resized = pd.DataFrame(data=resized_image, columns=[f'col{i}' for i in range(1, 151)])
df_resized.insert(0, 'depth', depths) # df_resized : store this in the db

# Connect to SQLite database to Store data
conn = sqlite3.connect('images.db')
c = conn.cursor()
# Create table if it does not exist
c.execute('''
CREATE TABLE IF NOT EXISTS images (
    depth REAL PRIMARY KEY,
    ''' + ', '.join([f'col{i} INTEGER' for i in range(1, 151)]) + '''
)
''')
# Insert data
df_resized.to_sql('images', conn, if_exists='replace', index=False)
conn.close()