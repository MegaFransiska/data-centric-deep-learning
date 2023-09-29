from metaflow import FlowSpec, step


class HelloFlow(FlowSpec):
    """
    A flow where Metaflow prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """

    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        print("HelloFlow is starting.")
        self.numbers = [1,2,3,4,5]
        self.next(self.count, foreach="numbers")

    @step
    def count(self):
        """
        A step for metaflow to introduce itself.

        """
        self.secret = self.input  #special variable
        print(f"Metaflow counts: {self.input}!")
        self.next(self.join)

    @step
    def join(self, inputs):
        self.secret = sum([x.secret for x in inputs])  # 15
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print(f"HelloFlow is all done. Secret: {self.secret}")


if __name__ == "__main__":
    HelloFlow()
