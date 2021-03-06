from torch.nn.modules.loss import _Loss


class FairseqCriterion(_Loss):

    def __init__(self, args, task):
        super().__init__()
        self.args = args
        self.padding_idx = task.target_dictionary.pad()

    @staticmethod
    def add_args(parser):
        """Add criterion-specific arguments to the parser."""
        pass

    def forward(self, model, sample, reduce=True):
        """Compute the loss for the given sample.

        Returns a tuple with three elements:
        1) the loss
        2) the sample size, which is used as the denominator for the gradient
        3) logging outputs to display while training
        """
        raise NotImplementedError

    @staticmethod
    def aggregate_logging_outputs(logging_outputs):
        """Aggregate logging outputs from data parallel training."""
        raise NotImplementedError

    def _aggregate_logging_outputs(self, logging_outputs):
        """An instance method version of :func:`aggregate_logging_outputs`.

        This can be overridden if needed, but please be careful not to rely
        on shared state when aggregating logging outputs otherwise you may
        get incorrect results.
        """
        return self.__class__.aggregate_logging_outputs(logging_outputs)

    @staticmethod
    def grad_denom(sample_sizes):
        """Compute the gradient denominator for a set of sample sizes."""
        return sum(sample_sizes)
