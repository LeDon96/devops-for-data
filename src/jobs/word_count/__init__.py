from operator import add


def get_keyval(row):
    word = filter(lambda r: r is not None, row)
    return [[w.strip().lower(), 1] for w in word]


def run(spark, config):
    df = spark.read.csv(config['relative_path'] + config['words_file_path'])

    mapped_rdd = df.rdd.flatMap(lambda row: get_keyval(row))
    counts_rdd = mapped_rdd.reduceByKey(add)
    return counts_rdd.collect()
