I2C_ADDRESS = 0x68 -- DS3231 address
I2C_REG = 0x00 -- DS3231 register pointer
I2C_ID = 0
SDA_PIN = 6
SCL_PIN = 7

i2c.setup(I2C_ID, SDA_PIN, SCL_PIN, i2c.SLOW)

function to_decimal(value)
    hl = bit.rshift(value, 4)
    hh = bit.band(value, 0xf)
    hr = string.format("%d%d", hl, hh)
    return string.format("%d%d", hl, hh)
end

function to_bcd(value)
    d = string.format("%d", tonumber(value / 10))
    d1 = tonumber(d * 10)
    d2 = value - d1
    return tonumber(d * 16 + d2)
end

function get_time()
    i2c.start(I2C_ID)
    i2c.address(I2C_ID, I2C_ADDRESS, i2c.TRANSMITTER)
    i2c.write(I2C_ID, I2C_REG)
    i2c.stop(I2C_ID)

    i2c.start(I2C_ID)
    i2c.address(I2C_ID, I2C_ADDRESS, i2c.RECEIVER)
    bytes = i2c.read(I2C_ID, 7)
    i2c.stop(I2C_ID)

    return to_decimal(string.byte(bytes, 1)), -- second
           to_decimal(string.byte(bytes, 2)), -- minute
           to_decimal(string.byte(bytes, 3)), -- hour
           to_decimal(string.byte(bytes, 4)), -- day of week
           to_decimal(string.byte(bytes, 5)), -- day of month
           to_decimal(string.byte(bytes, 6)), -- month
           to_decimal(string.byte(bytes, 7)) -- year
end

function get_time_iso_8601()
    second, minute, hour, day_of_week, day_of_month, month, year = get_time()
    return string.format("20%s-%s-%s-T%s:%s:%s", year, month, day_of_month, hour, minute, second)
end

function set_time(hour, minute, second, day_of_week, date, month, year)
    i2c.start(I2C_ID)
    i2c.address(I2C_ID, I2C_ADDRESS, i2c.TRANSMITTER)
    i2c.write(I2C_ID, I2C_REG)
    i2c.write(I2C_ID, to_bcd(second))
    i2c.write(I2C_ID, to_bcd(minute))
    i2c.write(I2C_ID, to_bcd(hour))
    i2c.write(I2C_ID, to_bcd(day_of_week))
    i2c.write(I2C_ID, to_bcd(date))
    i2c.write(I2C_ID, to_bcd(month))
    i2c.write(I2C_ID, to_bcd(year))
    i2c.stop(I2C_ID)
end
