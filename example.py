from .Nested.consumer import Consumer

if __name__ == "__main__":
    cons = Consumer()
    print(cons.get_count())
    cons.increment()
    print(cons.get_count())
    cons.decrement()
    print(cons.get_count())