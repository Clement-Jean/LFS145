# LFS145

This is the companion repository for the [LFS145 course](https://training.linuxfoundation.org/training/introduction-to-protocol-buffers-lfs145/).

## __Python__

In this section, we assume that you are in the `python` subdirectory.

### Virtual environment

#### __Creating__

```bash
python3 -m venv venv
```

#### __Activating__

For Linux/MacOS:

```bash
source venv/bin/activate
```

For Windows (Powershell):

```bash
./venv/bin/Activate.ps1
```

#### __Installing Dependencies__

```bash
pip3 install -r requirements.txt --upgrade
```

#### __Deactivating__

```bash
deactivate
```

### Running

```bash
python3 main.py [account|user|user2|product|phone|phone2|logine|logins|any|duration|duration2|time|fm|fm2|struct|struct2|wrapper|json|file]
```

### Protoc

```bash
protoc --python_out=. proto/*.proto
```

## __Java__

In this section, we assume that you are in the `java` subdirectory.

### Running

```bash
python3 ../python/main.py file
gradle run --args="$(PWD)/account.bin"
```