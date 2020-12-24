# Fastapi-docker-template

## 執行步驟
### 去申請免費網域
去[freenom](https://my.freenom.com/) 申請一個免費的網域做練習

![](https://i.imgur.com/fMpiNu9.jpg)
其中traefik.mb0520-demo.dl 就是我的子網域

### 建立.env 給docker-compose使用
```shell script
vim .env

# 舉例來說
DOMAIN=mb0520-demo.ml
EMAIL=meatball0520@gmail.com
TRAEFIK_USER=admin
TRAEFIK_PASSWORD_HASH=$2y$10$zi5n43jq9S63gBqSJwHTH.nCai2vB0SW/ABPGg2jSGmJBVRo0A.ni # admin


# 如果你要新增一筆賬號密碼 可以這樣設定
echo $(htpasswd -nb user password) | sed -e s/\\$/\\$\\$/g
# user:$$apr1$$nRnH1WwB$$UKQfB0zrDIKhocuSxc/tE.
```

### 建立憑證資訊
```shell script
touch acme.json
chmod 600 acme.json
```

## 還未完成的事情
- [ ] 理解trafik dashboard
- [ ] docker-compose.local.yml (for local traefik)

