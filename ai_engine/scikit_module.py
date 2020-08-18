import pandas as pd 
import numpy as np 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# classification/regression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import ExtraTreesClassifier, ExtraTreesRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
#regression
from sklearn.linear_model import LinearRegression

class Classifier:

    named_models = {
        "knn": KNeighborsClassifier,
        "rf": RandomForestClassifier,
        "extra_tree": ExtraTreesClassifier,
        "decision_tree": DecisionTreeClassifier,
        "ada_boost": AdaBoostClassifier,
        "gradient_boost": GradientBoostingClassifier
    }

    default_params = {
        "knn": {
            "n_neighbors": 5,
            "weights": "uniform",
            "leaf_size": 30,
            "p": 2
        },
        "rf": {
            "n_estimators": 100,
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
            "max_samples": None,
        },
        "extra_tree": {

            "n_estimators": 100,
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
            "max_samples": None,
        },
        "decision_tree": {

            "splitter": "best",
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
        },
        "ada_boost": {

            "base_estimator": None,
            "n_estimators": 50,
            "learning_rate": 1
        },
        "gradient_boost": {
            "loss": 'deviance',
            "learning_rate": 0.1,
            "n_estimators": 100,
            "max_depth": 3,
            "min_samples_split": 2,
            "min_samples_leaf": 1
        }
    }

    def __init__(self, model_name, parameters, dataset_path, split, method):
        self.model = None
        self.classes = None

        if model_name == "knn":
            if parameters == None:
                self.init_knn(self.default_params["knn"])
            else:
                self.init_knn(*parameters.values())
        
        if model_name == "rf":
            self.init_rf(*parameters.values())
        
        if model_name == "extra_tree":
            self.init_extra_tree(*parameters.values())
        
        if model_name == "decision_tree":
            self.init_decision_tree(*parameters.values())
        
        if model_name == "ada_boost":
            self.init_ada_boost(*parameters.values())
        
        if model_name == "gradient_boost":
            self.init_gradient_boost(*parameters.values())

        print(self.model)
        self.dataset = self.load_fit(dataset_path, split, method)
    
    """ fonctions to init each model with respective parameters """
    def init_knn(self, n_neighbors, weights, leaf_size, p):
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors, 
                                          weights=weights, 
                                          leaf_size=leaf_size, 
                                          p=p)

    def init_rf(self, n_estimators, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, max_samples):
        self.model = RandomForestClassifier(n_estimators=n_estimators, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes,
                                            max_samples=max_samples)

    def init_extra_tree(self, n_estimators, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, max_samples):
        self.model = ExtraTreesClassifier(n_estimators=n_estimators, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes,
                                            max_samples=max_samples)

    def init_decision_tree(self, splitter, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes):
        self.model = DecisionTreeClassifier(splitter=splitter, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes)
    
    def init_ada_boost(self, base_estimator, n_estimators, learning_rate):
        self.model = AdaBoostClassifier(base_estimator=base_estimator, 
                                        n_estimators=n_estimators, 
                                        learning_rate=learning_rate)
    
    def init_gradient_boost(self, loss, learning_rate, n_estimators, max_depth, min_samples_split, min_samples_leaf):
        self.model = GradientBoostingClassifier(loss=loss, 
                                          learning_rate=learning_rate, 
                                          n_estimators=n_estimators, 
                                          max_depth=max_depth,
                                          min_samples_split=min_samples_split,
                                          min_samples_leaf=min_samples_leaf)   

    """ Load dataset and fit the model """
    def load_fit(self, path, split, method):
        """
        line = open(path, "r").readlines()[0]
        line = line.split(",")
        features_size = len(line) - 1 # remove class column
        print("Features_size -> ", features_size)
        """
        df = pd.read_csv(path)

        if method == "drop":
            df = df.dropna()
            print(df)
        if method == "mean":
            df = df.fillna(df.mean())
            print(df)

        size = len(df[0])

        # preparing for training
        df = shuffle(df)
        
        X = np.array(df.drop(['class'], 1))
        y = np.array(df["class"])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=split)

        self.model.fit(X_train, y_train)
        self.classes = self.model.classes_

        print("Model " + path.split("/")[-1] + " test -> ", self.model.score(X_test, y_test))
        print("Model " + path.split("/")[-1] + " train -> ", self.model.score(X_train, y_train))

    """ returns predictions for each class """
    def predict(self, data):
        data = np.array(data).reshape(1,-1)
        #res = self.model.predict(data)
        probas = self.model.predict_proba(data)
       
        return self.classes, probas


class Regressor:

    named_models = {
        "knn": KNeighborsRegressor,
        "rf": RandomForestRegressor,
        "extra_tree": ExtraTreesRegressor,
        "decision_tree": DecisionTreeRegressor,
        "ada_boost": AdaBoostRegressor,
        "gradient_boost": GradientBoostingRegressor
    }

    default_params = {
        "knn": {
            "n_neighbors": 5,
            "weights": "uniform",
            "leaf_size": 30,
            "p": 2
        },
        "rf": {
            "n_estimators": 100,
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
            "max_samples": None,
        },
        "extra_tree": {

            "n_estimators": 100,
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
            "max_samples": None,
        },
        "decision_tree": {

            "splitter": "best",
            "max_depth": None,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_leaf_nodes": None,
        },
        "ada_boost": {

            "base_estimator": None,
            "n_estimators": 50,
            "learning_rate": 1
        },
        "gradient_boost": {
            "loss": 'deviance',
            "learning_rate": 0.1,
            "n_estimators": 100,
            "max_depth": 3,
            "min_samples_split": 2,
            "min_samples_leaf": 1
        }
    }

    def __init__(self, model_name, parameters, dataset_path, split):
        self.model = None
        self.classes = None

        if model_name == "knn":
            if parameters == None:
                self.init_knn(self.default_params["knn"])
            else:
                self.init_knn(*parameters.values())
        
        if model_name == "rf":
            self.init_rf(*parameters.values())
        
        if model_name == "extra_tree":
            self.init_extra_tree(*parameters.values())
        
        if model_name == "decision_tree":
            self.init_decision_tree(*parameters.values())
        
        if model_name == "ada_boost":
            self.init_ada_boost(*parameters.values())
        
        if model_name == "gradient_boost":
            self.init_gradient_boost(*parameters.values())

        print(self.model)
        self.dataset = self.load_fit(dataset_path, split)
    
    """ fonctions to init each model with respective parameters """
    def init_knn(self, n_neighbors, weights, leaf_size, p):
        self.model = KNeighborsRegressor(n_neighbors=n_neighbors, 
                                          weights=weights, 
                                          leaf_size=leaf_size, 
                                          p=p)

    def init_rf(self, n_estimators, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, max_samples):
        self.model = RandomForestRegressor(n_estimators=n_estimators, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes,
                                            max_samples=max_samples)

    def init_extra_tree(self, n_estimators, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, max_samples):
        self.model = ExtraTreesRegressor(n_estimators=n_estimators, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes,
                                            max_samples=max_samples)

    def init_decision_tree(self, splitter, max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes):
        self.model = DecisionTreeRegressor(splitter=splitter, 
                                            max_depth=max_depth, 
                                            min_samples_split=min_samples_split, 
                                            min_samples_leaf=min_samples_leaf,
                                            max_leaf_nodes=max_leaf_nodes)
    
    def init_ada_boost(self, base_estimator, n_estimators, learning_rate):
        self.model = AdaBoostRegressor(base_estimator=base_estimator, 
                                        n_estimators=n_estimators, 
                                        learning_rate=learning_rate)
    
    def init_gradient_boost(self, loss, learning_rate, n_estimators, max_depth, min_samples_split, min_samples_leaf):
        self.model = GradientBoostingRegressor(loss=loss, 
                                          learning_rate=learning_rate, 
                                          n_estimators=n_estimators, 
                                          max_depth=max_depth,
                                          min_samples_split=min_samples_split,
                                          min_samples_leaf=min_samples_leaf)   

    """ Load dataset and fit the model """
    def load_fit(self, path, split):

        df = pd.read_csv(path)
        df = shuffle(df)
        
        X = np.array(df.drop(['class'], 1))
        y = np.array(df["class"])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=split)

        self.model.fit(X_train, y_train)

        print("Model " + path.split("/")[-1] + " test -> ", self.model.score(X_test, y_test))
        print("Model " + path.split("/")[-1] + " train -> ", self.model.score(X_train, y_train))

    """ returns predictions for each class """
    def predict(self, data):
        data = np.array(data).reshape(1,-1)
        #res = self.model.predict(data)
        value = self.model.predict(data)
       
        return value

c = Classifier("knn", Classifier.default_params["knn"], "dataset.csv", split=0.2, method="mean")

print(c.predict([1,2,4,3,1]))
