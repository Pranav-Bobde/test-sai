from flask import Flask, request, make_response
from io import BytesIO

    
# Perform your desired processing with the prompt
# For example, you can use the DiffusionPipeline code you provided

from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.enable_model_cpu_offload()



app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_prompt():
    prompt = request.get_json()['prompt']

    image = pipe(prompt=prompt).images[0]

    # Convert the image to bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    
    # Create the response with the image bytes
    response = make_response(img_bytes)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='image.png')
    
    return response
    
    @app.route('/hello', methods=['GET'])
    def hello_world():
        return 'Hello World'
    
    if __name__ == '__main__':
    app.run()