{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Streamlit Image Classification Web App",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lawliaet/ds/blob/main/Streamlit_Image_Classification_Web_App.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j5C8c_IfYHfH",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 698
        },
        "outputId": "7193ce66-c717-4d2b-c7fa-52152cee25c7"
      },
      "source": [
        "!pip install -U ipykernel==5.3.4"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting ipykernel==5.3.4\n",
            "  Downloading ipykernel-5.3.4-py3-none-any.whl (120 kB)\n",
            "\u001b[K     |████████████████████████████████| 120 kB 4.8 MB/s \n",
            "\u001b[?25hRequirement already satisfied: ipython>=5.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.5.0)\n",
            "Requirement already satisfied: traitlets>=4.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.1.1)\n",
            "Requirement already satisfied: tornado>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.1.1)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.3.5)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (4.4.2)\n",
            "Requirement already satisfied: pexpect in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (4.8.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (2.6.1)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (0.7.5)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (1.0.18)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (57.4.0)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (0.8.1)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=5.0.0->ipykernel==5.3.4) (0.2.5)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=5.0.0->ipykernel==5.3.4) (1.15.0)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (23.0.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (2.8.2)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (4.10.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect->ipython>=5.0.0->ipykernel==5.3.4) (0.7.0)\n",
            "Installing collected packages: ipykernel\n",
            "  Attempting uninstall: ipykernel\n",
            "    Found existing installation: ipykernel 4.10.1\n",
            "    Uninstalling ipykernel-4.10.1:\n",
            "      Successfully uninstalled ipykernel-4.10.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires ipykernel~=4.10, but you have ipykernel 5.3.4 which is incompatible.\u001b[0m\n",
            "Successfully installed ipykernel-5.3.4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "ipykernel"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rrVDYLxxMzxz"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uxclE-m8LZa6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "dad8c59c-a781-4396-c412-8b1a5b9379aa"
      },
      "source": [
        "!pip install -q streamlit"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 9.1 MB 4.8 MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.3 MB 51.2 MB/s \n",
            "\u001b[K     |████████████████████████████████| 232 kB 67.0 MB/s \n",
            "\u001b[K     |████████████████████████████████| 77 kB 6.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 164 kB 52.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 111 kB 66.7 MB/s \n",
            "\u001b[K     |████████████████████████████████| 181 kB 65.7 MB/s \n",
            "\u001b[K     |████████████████████████████████| 63 kB 2.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 51 kB 8.6 MB/s \n",
            "\u001b[?25h  Building wheel for blinker (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j-qizgiOFEkc",
        "outputId": "839d087f-7dc7-4959-acbe-4b8e4339ff31"
      },
      "source": [
        "!wget https://bin.equinox.io/c/4VmDzA7iaHb/-stablngroke-linux-amd64.zip"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-06-07 16:11:45--  https://bin.equinox.io/c/4VmDzA7iaHb/-stablngroke-linux-amd64.zip\n",
            "Resolving bin.equinox.io (bin.equinox.io)... 52.202.168.65, 54.161.241.46, 54.237.133.81, ...\n",
            "Connecting to bin.equinox.io (bin.equinox.io)|52.202.168.65|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 13832437 (13M) [application/octet-stream]\n",
            "Saving to: ‘-stablngroke-linux-amd64.zip’\n",
            "\n",
            "-stablngroke-linux- 100%[===================>]  13.19M  5.39MB/s    in 2.4s    \n",
            "\n",
            "2022-06-07 16:11:48 (5.39 MB/s) - ‘-stablngroke-linux-amd64.zip’ saved [13832437/13832437]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MrUFFcWtFIC_",
        "outputId": "01e4ee4e-6aa7-4434-8afe-c8cebd5bc78d"
      },
      "source": [
        "!unzip /content/-stablngroke-linux-amd64.zip"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  /content/-stablngroke-linux-amd64.zip\n",
            "  inflating: ngrok                   \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DEpqpO_1FNWJ",
        "outputId": "2f8d7239-f607-43c0-d0b9-f1a04beefeaa"
      },
      "source": [
        "!ls"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "drive  ngrok  sample_data  -stablngroke-linux-amd64.zip\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hVZv2sH3FRzo",
        "outputId": "e2c5566d-c1c1-4255-81a7-3b7e8101cb45"
      },
      "source": [
        "!./ngrok "
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NAME:\n",
            "   ngrok - tunnel local ports to public URLs and inspect traffic\n",
            "\n",
            "DESCRIPTION:\n",
            "    ngrok exposes local networked services behinds NATs and firewalls to the\n",
            "    public internet over a secure tunnel. Share local websites, build/test\n",
            "    webhook consumers and self-host personal services.\n",
            "    Detailed help for each command is available with 'ngrok help <command>'.\n",
            "    Open http://localhost:4040 for ngrok's web interface to inspect traffic.\n",
            "\n",
            "EXAMPLES:\n",
            "    ngrok http 80                    # secure public URL for port 80 web server\n",
            "    ngrok http -subdomain=baz 8080   # port 8080 available at baz.ngrok.io\n",
            "    ngrok http foo.dev:80            # tunnel to host:port instead of localhost\n",
            "    ngrok http https://localhost     # expose a local https server\n",
            "    ngrok tcp 22                     # tunnel arbitrary TCP traffic to port 22\n",
            "    ngrok tls -hostname=foo.com 443  # TLS traffic for foo.com to port 443\n",
            "    ngrok start foo bar baz          # start tunnels from the configuration file\n",
            "\n",
            "VERSION:\n",
            "   2.3.40\n",
            "\n",
            "AUTHOR:\n",
            "  inconshreveable - <alan@ngrok.com>\n",
            "\n",
            "COMMANDS:\n",
            "   authtoken\tsave authtoken to configuration file\n",
            "   credits\tprints author and licensing information\n",
            "   http\t\tstart an HTTP tunnel\n",
            "   start\tstart tunnels by name from the configuration file\n",
            "   tcp\t\tstart a TCP tunnel\n",
            "   tls\t\tstart a TLS tunnel\n",
            "   update\tupdate ngrok to the latest version\n",
            "   version\tprint the version string\n",
            "   help\t\tShows a list of commands or help for one command\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a3gBR5EsiIa7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8c659170-9c56-4bfe-9b41-81265d2b8cf0"
      },
      "source": [
        "!pip install pyngrok==4.1.8"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyngrok==4.1.8\n",
            "  Downloading pyngrok-4.1.8.tar.gz (19 kB)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.8) (0.16.0)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.8) (3.13)\n",
            "Building wheels for collected packages: pyngrok\n",
            "  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyngrok: filename=pyngrok-4.1.8-py3-none-any.whl size=16348 sha256=06c7db837d50298d33eaefb19a7ee0b7d79559fdd391b2ae83b5683619794bd4\n",
            "  Stored in directory: /root/.cache/pip/wheels/63/49/e3/03bfea32f8f48ae169091003ecd82f7ac6a598c9683326f995\n",
            "Successfully built pyngrok\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-4.1.8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xEjZmh1V078P"
      },
      "source": [
        "https://ngrok.com/\n",
        "\n",
        "⚠️⚠️Update the token below from creating an account in ngrok website⚠️⚠️\n",
        "\n",
        "You can ignore Ngrok step completely if you are not looking to expose your app to internet\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YjoAEsIEh-oZ",
        "cellView": "both",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2fc9f1d4-38f5-4ec0-f80c-40065c4ccfea"
      },
      "source": [
        "!./ngrok authtoken 21j68CC03JWN6TY2Vh9sqDABXib_2JYYHuEduf95MSPoDYz6z"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hvmlfY16Yg9O",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "60937ef2-b965-43fa-a4f4-bfeb0c47a522"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!unzip /content/drive/MyDrive/chess_model.zip"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HbVuuqLz-nTy",
        "outputId": "d4ffd8a0-ac51-4924-d429-5e44d478ac27"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  /content/drive/MyDrive/chess_model.zip\n",
            "   creating: content/chess_model/\n",
            "   creating: content/chess_model/variables/\n",
            "  inflating: content/chess_model/variables/variables.data-00000-of-00001  \n",
            "  inflating: content/chess_model/variables/variables.index  \n",
            "  inflating: content/chess_model/saved_model.pb  \n",
            "   creating: content/chess_model/assets/\n",
            "  inflating: content/chess_model/keras_metadata.pb  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RuNpGDdZY3WW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2e559b45-4da5-4c78-ab66-6e38b68f9b4c"
      },
      "source": [
        "%%writefile score.py\n",
        "\n",
        "import tensorflow as tf\n",
        "import numpy as np\n",
        "import streamlit as st\n",
        "from PIL import Image\n",
        "import requests\n",
        "from io import BytesIO\n",
        "\n",
        "st.set_option('deprecation.showfileUploaderEncoding', False)\n",
        "st.title(\"Image Classifier\")\n",
        "st.text(\"Provide URL of flower Image for image classification\")\n",
        "\n",
        "@st.cache(allow_output_mutation=True)\n",
        "def load_model():\n",
        "  model = tf.keras.models.load_model('/content/content/chess_model')\n",
        "  return model\n",
        "\n",
        "with st.spinner('Loading Model Into Memory....'):\n",
        "  model = load_model()\n",
        "\n",
        "classes=['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook']\n",
        "\n",
        "\n",
        "def scale(image):\n",
        "  image = tf.cast(image, tf.float32)\n",
        "  image /= 255.0 # external data norm while training\n",
        "  # in our case norm is part of sequential model\n",
        "\n",
        "  return tf.image.resize(image,[224,224])\n",
        "\n",
        "def decode_img(image):\n",
        "  img = tf.image.decode_jpeg(image, channels=3)\n",
        "  img = scale(img)\n",
        "  return np.expand_dims(img, axis=0)\n",
        "\n",
        "path = st.text_input('Enter Image URL to Classify.. ','https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg')\n",
        "image_file = st.file_uploader(\"Upload Images\", type=[\"png\",\"jpg\",\"jpeg\"])\n",
        "if path is not None:\n",
        "    content = requests.get(path).content\n",
        "\n",
        "    st.write(\"Predicted Class :\")\n",
        "    with st.spinner('classifying.....'):\n",
        "      label =np.argmax(model.predict(decode_img(content)),axis=1)\n",
        "      st.write(np.array(classes))\n",
        "      st.write(model.predict(decode_img(content)))\n",
        "      st.write(classes[label[0]])    \n",
        "    st.write(\"\")\n",
        "    image = Image.open(BytesIO(content))\n",
        "    st.image(image, caption='Classifying Bean Image', use_column_width=True)    \n"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing score.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zhFjAjHFP62u"
      },
      "source": [
        "# import tensorflow as tf\n",
        "# model = tf.keras.models.load_model('/content/drive/MyDrive/Colab Notebooks/models/flower/models')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZeUbOXBNhVmq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "effc2ecb-0484-4e3a-e37a-91ce2363234e"
      },
      "source": [
        "!nohup streamlit run score.py >/dev/null &"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nohup: redirecting stderr to stdout\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run score.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIZfUBEmzmQf",
        "outputId": "e18433af-fe42-426e-9669-84fb0bb7bc1d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2022-06-07 11:20:18.299 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 2.117s\n",
            "your url is: https://warm-hats-remain-34-73-109-20.loca.lt\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.73.109.20:8501\u001b[0m\n",
            "\u001b[0m\n",
            "2022-06-07 11:20:48.934774: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YB0kwgXqhdeo",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "0ad56514-72a3-4273-beaa-3926d177ee68"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "url = ngrok.connect(port=8503)\n",
        "url"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'http://b34b-34-73-109-20.ngrok.io'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "71SR5W0rkrsw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d7d5a570-f3ed-4877-ff79-1ffc25471604"
      },
      "source": [
        "!cat nohup.out"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cat: nohup.out: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mvmVgcgCODxD"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
