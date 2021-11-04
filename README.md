<h1 align="center"> Image Deep Hash </h1>

**Information Integrity Checking** is one of the important uses of hash functions. However, current hash functions such as **SHA**, **MD**, etc. only tell us the integrity of the file, but do not tell us how much the information has changed.

---

For an image that only needs to be 1 pixel different, the hash results will be completely different. In some cases like loading a 60fps video and only 1 frame is 1 pixel wrong, reloading is too expensive. We overcome that problem by extracting features of the image to evaluate the difference between the downloaded image and the original image and then make a decision whether it is necessary to reload or not. However, the solution also has limitations in having high time and space complexity.

## 🌟 **Run on localhost (require CUDA)**
- Clone the repo
```
git clone https://github.com/lannguyen0910/image-deep-hash
cd image-deep-hash/
```
- Install dependencies
```
pip install -r requirements.txt
```
- Start the app
```
python app.py --host=localhost:3000
```

## 🌟 **Run using Google Colab**
Open notebook and follow the instructions [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N2AyKf_G8ImdRdpgpzLbyQf0PgH7jwlt?usp=sharing)

## 🌟 **Deep Hash**
Hash an image and return to a hash sequence which its hex length is modifiable. Go to <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/examples/hash/hash_tutorial.ipynb">hash_tutorial</a> and <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/src/ImageDeepHash.py">hash_module</a> for more information

```python
from src import ImageDeepHash

m = ImageDeepHash.ImageDeepHash()
m.hash("ILSVRC2012_val_00005002.jpeg")
print(m.digest())
print(m.hexdigest())
m.plot()
```

<p align="center">
  <img src="./examples/images/Hash_From_Code_1.PNG" width="300" title="Compare example 1">
</p>

```python
m.reset()
m.hash("ILSVRC2012_val_00005002_noise.jpeg")
print(m.digest())
print(m.hexdigest())
m.plot()
```

<p align="center">
  <img src="./examples/images/Hash_From_Code_2.PNG" width="300" title="Compare example 1">
</p>

<b>Run on <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/app.py">web</a></b>:
<p align="center">
  <img src="./examples/images/hash_1.PNG" width="400" title="Compare example 1">
  <img src="./examples/images/hash_2.PNG" width="400" title="Compare example 2">
</p>

## 🌟 **Deep Compare**
Hash 2 images and evaluate the difference using some appropriate metrics for comparision. Go to <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/examples/compare/compare_tutorial.ipynb">compare_tutorial</a> and <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/src/ImageDeepCompare.py">compare_module</a> for more information

```python
from src import ImageDeepCompare

m = ImageDeepCompare.ImageDeepCompare()
print("Distance:", m.compare("ILSVRC2012_val_00005002.jpeg", "ILSVRC2012_val_00005002_noise.jpeg", "euclidean"))
m.plot()
```

<p align="center">
  <img src="./examples/images/Compare_From_Code.PNG" width="500" title="Compare example 1">
</p>
 
<b>Run on <a href="https://github.com/lannguyen0910/image-deep-hash/blob/main/app.py">web</a></b>:
<p align="center">
  <img src="./examples/images/compare_1.PNG?raw=True" width="600" title="Compare example 1">
  </br>
  <img src="./examples/images/compare_2.PNG?raw=True" width="300" alt="Compare example 1 result">
</p>

