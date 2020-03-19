#!//usr/bin/python3
"""Dictionary with the names of all the photographed birds in the database Birds.
"""
from PIL import Image
import sys

def main():
        print("In our beta stages we are only offering a few birds at the moment: \
            \n Alexandrine Parakeet, American Goldfinch, \
            \n Black Swan ,Curl Crested Aracuri,\
            \n Quetzal and, Rainbow Lorikeet.")
        user_bird = input("Which would you like to see? q to quit ")
        if user_bird == 'q':
            sys.exit()
        user_photo = input("Each bird has 5 photos take your pick! q to quit ")
        if user_photo == 'q':
            sys.exit()
        user_choice = birds[user_bird][user_photo]
        img_appear = Image.open(user_choice)
        try:
            img_appear.show()
        except IOError:
            pass

birds = {'American Goldfinch': {'1': '~/Bird-visual-reference/test case birbs/AMERICAN GOLDFINCH/1.jpg', 
                                '2': '~/Bird-visual-reference/test case birbs/AMERICAN GOLDFINCH/2.jpg',
                                '3': '~/Bird-visual-reference/test case birbs/AMERICAN GOLDFINCH/3.jpg',
                                '4': '~/Bird-visual-reference/test case birbs/AMERICAN GOLDFINCH/4.jpg',
                                '5': '~/Bird-visual-reference/test case birbs/AMERICAN GOLDFINCH/5.jpg'},
 'Alexandrine Parakeet': {'1':'/Users/liamk./Downloads/Bird-visual-reference/test case birbs/ALEXANDRINE PARAKEET/1.jpg',
                         '2': '/Bird-visual-reference/test case birbs/ALEXANDRINE PARAKEET/2.jpg', 
                         '3': '/Bird-visual-reference/test case birbs/ALEXANDRINE PARAKEET/3.jpg', 
                         '4': '/Bird-visual-reference/test case birbs/ALEXANDRINE PARAKEET/4.jpg', 
                         '5': '/Bird-visual-reference/test case birbs/ALEXANDRINE PARAKEET/5.jpg'}, 
 'Black Swan': {'1': '/Bird-visual-reference/test case birbs/BLACK SWAN/1.jpg',
                '2': '/Bird-visual-reference/test case birbs/BLACK SWAN/2.jpg',
                '3': '/Users/liamk./Downloads/Bird-visual-reference/test case birbs/BLACK SWAN/3.jpg',
                '4': '/Bird-visual-reference/test case birbs/BLACK SWAN/4.jpg',
                '5': '/Bird-visual-reference/test case birbs/BLACK SWAN/5.jpg'},
 'Curl Crested Aracuri': {'1': '/Bird-visual-reference/test case birbs/CURL CRESTED ARACURI/1.jpg',
                        '2': '/Bird-visual-reference/test case birbs/CURL CRESTED ARACURI/2.jpg',
                        '3': '/Bird-visual-reference/test case birbs/CURL CRESTED ARACURI/3.jpg',
                        '4': '/Bird-visual-reference/test case birbs/CURL CRESTED ARACURI/4.jpg',
                        '5': '/Bird-visual-reference/test case birbs/CURL CRESTED ARACURI/5.jpg'},
 'Quetzal': {'1': '~/Bird-visual-reference/test case birbs/QUETZAL/1.jpg',
            '2': '~/Bird-visual-reference/test case birbs/QUETZAL/2.jpg',
            '3': '~/Bird-visual-reference/test case birbs/QUETZAL/3.jpg',
            '4': '~/Bird-visual-reference/test case birbs/QUETZAL/4.jpg',
            '5': '~/Bird-visual-reference/test case birbs/QUETZAL/5.jpg'},
 'Rainbow Lorikeet': {'1': '~/Bird-visual-reference/test case birbs/RAINBOW LORIKEET/1.jpg', 
                    '2': '~/Bird-visual-reference/test case birbs/RAINBOW LORIKEET/2.jpg', 
                    '3': '~/Bird-visual-reference/test case birbs/RAINBOW LORIKEET/3.jpg', 
                    '4': '~/Bird-visual-reference/test case birbs/RAINBOW LORIKEET/4.jpg', 
                    '5': '~/Bird-visual-reference/test case birbs/RAINBOW LORIKEET/5.jpg'}}

if __name__ == "__main__":
    main()
    