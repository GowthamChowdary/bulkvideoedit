from moviepy.editor import *
for i in range(10):
	string=str(i)+".mp4"
	clip1=VideoFileClip(string)
	interval=VideoFileClip('int.mov')
	interval=interval.resize( (1920,1080) )
	edited1=clip1.subclip(30,480)
	edited2=clip1.subclip(481,960)
	edited3=clip1.subclip(961,1250)
	final_clip = concatenate_videoclips([edited1,interval])
	second_clip=concatenate_videoclips([edited2,interval])
	thrid_clip=concatenate_videoclips([final_clip,second_clip])
	end_clip=concatenate_videoclips([thrid_clip,edited3])
	final_string=str(i)+"converted"

	end_clip.write_videofile(final_string,codec='libx264')


