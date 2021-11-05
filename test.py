from blur_image import blur
# blur(source, output, mode = "simple")
# Modes: simple, box, gaussian
# Value is available for this modes: box, gaussian
blur("onur_profile_photograph.jpg", "blurred_source.jpg")
blur("onur_profile_photograph.jpg", "blurred_source_2.jpg", mode = "box", value = 5)
blur("onur_profile_photograph.jpg", "blurred_source_3.jpg", mode = "gaussian", value = 5)