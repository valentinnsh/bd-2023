## Вопросы
1. Страничная организация памяти в современных операционных системах. Устройства процессоров - кэш, многоядерность. Файл подкачки, memory mapped files.
2. Примитивы синхронизации потоков и процессов в Python (блокировки, семафоры, барьеры, очереди с приоритетом, каналы (`Pipes`)), пулы потоков/процессов,  `Future`/`AsyncResult`). Вопрос не затрагивает `asyncio`.
3. Модуль `multiprocessing`, запуск дочерних процессов, использование общей памяти между процессами (в том числе общие массивы `NumPy`), средства межпроцессорного взаимодействия (очереди, каналы (`Pipes`)). Способы запуска дочерних процессов (`fork`, `forkserver`, `spawn`).
4. Изоляция процессов, контейнеризация. Механизмы ядра `Linux` (`namespaces`, `cgroups`). Отличие от виртуализации (гипервизоров 1, 2 типов). Основы Docker.
5. Основные концепции `Docker`: контейнер, образ. Управление контейнерами. `Dockerfile`. 
6. Контейнеризация приложений на Python, основные правила написания `Dockerfile` - эффективное использование кэша. Docker compose. 
7. Термин `Big Data`. История возникновения явления. Концепция трех "V". NoSql базы данных, колоночная организация хранения. `OLAP`, `OLTP`. 
8. Устройство `HDFS`. Гарантии согласованности. Репликация данных. Организация кластера. `YARN` (Yet Another Resource Negotiator).
9. Модель вычислений `map reduce`. `Hadoop`.  Стадии выполнения задачи. `Data locality`.
10. `Apache Hive`. Сфера применения, выполнение задач, особенности языка запросов, гарантии согласованности. `Apache HBase`, модель данных и архитектура. 
11. `Apache Zookeeper`. Сфера применения, основные возможности, отказоустойчивость. Поддержка согласованности данных.
12. `Apache Spark`, общая архитектура. `RDD`. Алгоритм `HyperLogLog`.
13. `Spark SQL` & `DataFrames` - мотивация перехода с `RDD`.  Особенности клиента для  `Python` - `PySpark`. Повышение производительности. Взаимодействие c  `Pandas`. Использование `GraphX`и `MLlib` (*). 
14. `Dask` и `Ray`. Устройство, возможности, области применения. 
15. Локальная работа с большими данными. `Apache Arrow`, `SQLite`, `DuckDB`. Взаимодействие с `Pandas`.
16. Распределенные системы и согласованность данных в распределенных системах: "теорема" CAP. Strong, Sequential, Eventual Consistency. 
17. Алгоритмы консенсуса в распределенных системах. `Paxos` и `Raft`.


## Литература:
1. https://assets.bitbashing.io/papers/concurrency-primer.pdf (Q1, Q2, Q3)
2. https://docs.docker.com/get-started/ (Q4, Q5)
3. https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ (Q5, Q6)
4. https://github.com/heathermiller/dist-prog-book (Q1, Q2, Q3, Q6)
5. https://docs.python.org/3/library/multiprocessing.html (Q3)
6. https://docs.python.org/3/library/concurrent.futures.html (Q3)
7. http://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf (Q3)
8. https://hadoop.apache.org/docs/current/hdfs_design.html (Q8)
9. https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html (Q8)
10. https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html (Q9)
11. https://zookeeper.apache.org/doc/current/zookeeperStarted.html (Q11)
12. https://hive.apache.org/ (Q10)
13. https://hbase.apache.org/ (Q10)
14. https://spark.apache.org/ (Q12, Q13)
15. https://spark.apache.org/sql/ (Q12, Q13)
16. https://dask.org (Q14)
17. https://ray.io (Q14)
18. https://arrow.apache.org (Q15)
19. https://arrow.apache.org/docs/python/index.html (Q15)
20. https://duckdb.org/docs/guides/python/install (Q15)
21. https://en.wikipedia.org/wiki/Consistency_model (Q16)
22. https://xzhu0027.gitbook.io/blog/misc/index/consistency-models-in-distributed-system (Q16, Q17)
23. https://jepsen.io/consistency (Q16)
24. https://en.wikipedia.org/wiki/Paxos_(computer_science) (Q17)
25. https://raft.github.io/ (Q17)
26. https://raft.github.io/raft.pdf (Q17)
27. https://en.wikipedia.org/wiki/Paxos_(computer_science) (Q17)

Data:
https://drive.google.com/file/d/1XQDEPEQxJQgnmLX3idlsh-WDTnj0y7ul/view