import argparse
import img_match
import importlib


def find_templateclass_using_name(class_num):
    templateclass_name = "DegreeToNum.templateclass" + str(class_num)
    print(templateclass_name)
    templateclass = importlib.import_module(templateclass_name)

    if templateclass is None:
        raise NotImplementedError("In DegreeToNum package, the model %s not find." % (templateclass_name))

    return templateclass


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--img_path", type=str, default="./img_test/test1.png",
                    help='the path of the test image')
parser.add_argument("--template_dir", type=str, default="./template/",
                    help='the dir of template images')
parser.add_argument("--siftedimg_dir", type=str, default="./img_test_corrected/",
                    help='the dir of sifted images')

opt, _ = parser.parse_known_args()

# find the right template and correct the image
queryImagePath = opt.img_path
templateImgDir = opt.template_dir
outImg = opt.siftedimg_dir
print(opt)
matchedTemplateClass = img_match.CorrectImage(queryImagePath, templateImgDir, outImg)
print(matchedTemplateClass)

# check the pointer position and compute the num according to the degree of pointer
if matchedTemplateClass is None:
    raise ValueError("no find the right template class")

corrected_img_path = outImg + queryImagePath.split("/")[-1]
templateclass = find_templateclass_using_name(matchedTemplateClass)

num = templateclass.degree2num(corrected_img_path)
print(num)
