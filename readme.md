# General description
Comparison of SVM with BP and Linear Regression

### Objective
Compare the classification results with the following algorithms:
* Support Vector Machines (SVM), using free software
* Back-Propagation (BP), implemented by the student
* Multiple Linear Regression (MLR), using free software

### Data
* File: 
	- Training: ring-separable.txt, ring-merged.txt
	![alt text](https://github.com/CarlosJesusGH/URV_NEC_MachineLearning_MethodComparison/blob/master/screenshot/Screenshot%20from%202017-06-28%2010-24-29.png?raw=true)
	- Test: ring-test.txt
* Columns: 2 variables, 1 value to predict
    - Variables:
        - x ϵ [-1,1]
        - y ϵ [-1,1]
    - Prediction: class of the pattern, either 0 or 1
        - ring-separable.txt: class 1) inside a ring of internal radius 0.2 and external radius 0.8; class 0) outside the ring, inside a square of sides between -1 and 1
        - ring-merged.txt: here the belonging to each class depends on a probability distribution which is a function of the distance to the center of the ring. The Bayesian decision boundary between both classes is once again the circles of radii 0.2 and 0.8 respectively, in such a way that class 1 is more likely inside the ring, and class 0 outside it.
* Patterns: 10000 patterns
    - Training and Validation: all the patterns, or the subsets you prefer
    - Test: all the patterns in ring-test.txt

