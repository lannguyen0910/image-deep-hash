# **Image Deep Hash**
**Information Integrity Checking** is one of the important uses of hash functions. However, current hash functions such as **SHA**, **MD**, etc. only tell us the integrity of the file, but do not tell us how much the information has changed.

---

For an image that only needs to be 1 pixel different, the hash results will be completely different. In some cases like loading a 60fps video and only 1 frame is 1 pixel wrong, reloading is too expensive. We overcome that problem by extracting features of the image to evaluate the difference between the downloaded image and the original image and then make a decision whether it is necessary to reload or not. However, the solution also has limitations in having high time and space complexity.

## **Deep Hash**

## **Deep Compare**

## **Run using Google Colab with Ngrok**
- Open notebook and follow the instructions [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N2AyKf_G8ImdRdpgpzLbyQf0PgH7jwlt?usp=sharing)
