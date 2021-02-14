# セットアップ

## pigpioのインストール

``` 

$ sudo apt update
$ sudo apt upgrade
$ sudo apt install pigpio python3-pigpio
$ sudo systemctl enable pigpiod.service    # ラズパイ再起動時に pigpiod を自動的に起動させます
$ sudo systemctl start pigpiod             # いますぐ pigpiod を起動
```

## GPIOの設定

``` 

$ echo 'm 27 w   w 27 0   m 4 r   pud 4 u   m 5 r   pud 5 u' > /dev/pigpio

$ crontab -e
以下を追記
@reboot until echo 'm 27 w   w 27 0   m 4 r   pud 4 u   m 5 r   pud 5 u' > /dev/pigpio; do sleep 1s; done
```

## 必要なパッケージ

flask
requests

https://korintje.com/archives/28
