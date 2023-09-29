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
        self.next(self.hello, self.howareyou)

    @step
    def hello(self):
        """
        A step for metaflow to introduce itself.

        """
        print("Metaflow says: Hi!")
        self.secret = 1
        self.next(self.join)

    @step
    def howareyou(self):
        print("Metaflow says: How are you?")
        self.secret = 2
        self.next(self.join)

    @step
    def join(self, inputs):
        self.secret = inputs.hello.secret + inputs.howareyou.secret  # 2
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
