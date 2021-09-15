# ImageDeepHash
## Deep Hash
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

<b>Or using <a href="https://github.com/ffyyytt/ImageDeepHash#run-using-google-colab-with-ngrok">website</a></b>:
<p align="center">
  <img src="./examples/images/hash_1.PNG" width="400" title="Compare example 1">
  <img src="./examples/images/hash_2.PNG" width="400" title="Compare example 2">
</p>

## Deep Compare
```python
from src import ImageDeepCompare

m = ImageDeepCompare.ImageDeepCompare()
print("Distance:", m.compare("ILSVRC2012_val_00005002.jpeg", "ILSVRC2012_val_00005002_noise.jpeg", "euclidean"))
m.plot()
```
<p align="center">
  <img src="./examples/images/Compare_From_Code.PNG" width="500" title="Compare example 1">
</p>
 
<b>Or using <a href="https://github.com/ffyyytt/ImageDeepHash#run-using-google-colab-with-ngrok">website</a></b>:
<p align="center">
  <img src="https://github.com/ffyyytt/ImageDeepHash/blob/main/examples/images/compare_1.PNG?raw=True" width="600" title="Compare example 1">
  </br>
  <img src="https://github.com/ffyyytt/ImageDeepHash/blob/main/examples/images/compare_2.PNG?raw=True" width="300" alt="Compare example 1 result">
</p>
## **Run using Google Colab with Ngrok**
- Open notebook and follow the instructions [![Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N2AyKf_G8ImdRdpgpzLbyQf0PgH7jwlt?usp=sharing)
