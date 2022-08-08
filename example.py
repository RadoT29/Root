from .Nested.consumer import Consumer

if __name__ == "__main__":
    cons = Consumer()
    print(cons.get_count())
    cons.increment(5)
    print(cons.get_count())
    cons.decrement()
    print(cons.get_count())