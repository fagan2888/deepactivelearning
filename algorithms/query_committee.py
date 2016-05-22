#-------------------------------
# Query By Committee - active learning through QBC
#
#
#-------------------------------

class QueryByCommittee(object):
    def __init__(self):
        """
        label_training: initial set of labeled training examples (can be empty)
        set_labeled: set of labeled training examples
        """
        label_training = None
        set_labeled = None
        committees = None

    def construct_commitee(N, p_d, n):
        """
        Constructs a committee/partial nn from the parameters:
        N: full network
        p_d: dropout probability
        n: committee size
        """

    def last_layer_backprop(N, input_score, predicted_score, num):
        """
        Backpropogation but only through the last num layers of the nn
        N: full network
        input_score: training score
        predicted_score: score outputted by committees
        num: backprop backwards num layers
        """

    def oracle(S):
        """
        S: S contains batch_size elements
        We want to update label_training and set_labeled with these elements
        """

    def train_committee(batch_size):
        """
        trains random samples on committees, outputs batch_size samples
        """
    
    def run(...):
        """
        runs abc
        """
