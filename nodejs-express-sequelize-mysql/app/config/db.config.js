module.exports = {
  HOST: "localhost",
  USER: "dev",
  PASSWORD: "GodMode@94",
  DB: "appdb",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
};
