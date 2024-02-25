HMC5883L may not activate by default.
Must run this command to activate first

```sh
i2cset -y 1 0x68 0x37 0x02
i2cset -y 1 0x68 0x6a 0x00
i2cset -y 1 0x68 0x6b 0x00
```

then set continuous measurement mode
```sh
i2cset -y 1 0x68 0x02 0x00
```
