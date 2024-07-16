from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    try:
        inp = Image.open(input_path)
        
        output = remove(inp)
        
        output.save(output_path, format="PNG")
        
        print(f"image with background removed successfully recorded: {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

# Kullanım örneği
if __name__ == "__main__":
    input_path = "tesla.png"
    output_path = "tesla_no_bg.png"
    
    remove_background(input_path, output_path)
