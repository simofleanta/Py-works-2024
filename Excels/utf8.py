df = df.applymap(lambda x: x.encode('utf-8').decode('utf-8') if isinstance(x, str) else x)
