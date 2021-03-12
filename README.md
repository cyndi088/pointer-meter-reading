# SIFT-Hough-for-multi-type-pointer-meter-reading

## Flow-chart
![](./picture/flow-chart.jpg)

## Preparation

### Pre-requisites
* Python 3.6
* opencv-python = 3.4.2
* numpy = 1.18.5

### Installation

* git clone code

```bash
$ git clone https://github.com/tangzhenjie/SIFT-and-Hough-for-multi-type-pointer-meter-reading.git
```

* the directories structure

```
  Framework                           
  ├── DegreeToNum        % the dir storing the model for each template
  ├── img_test           % the dir storing the test image (suggested)
  ├── img_test_corrected % the dir storing the corrected images (suggested)
  ├── template           % the dir storing the template images
  ├── img_match.py       % the sift matching code
  └── read_num.py        % the main code
```

### Run

```bash
python read_num.py $your_test_img_path
```

## Result
![](./picture/example.jpg)

![](./picture/result2.jpg)



