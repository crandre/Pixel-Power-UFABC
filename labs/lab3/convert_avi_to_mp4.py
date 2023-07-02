from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec="libx264")
    clip.close()

# Example usage
input_file = "./labs/lab3/saida3_blur.avi"
output_file = "./saida3_blur.mp4"
convert_avi_to_mp4(input_file, output_file)
