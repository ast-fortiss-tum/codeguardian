// From JSVulnerabilityDataSet, row no.69 and no.70 .

function Airbrake() {
    this.key = null;
  
    this.host = 'https://' + os.hostname();
    this.env = process.env.NODE_ENV || 'development';
    this.projectRoot = null;
    this.appVersion = null;
    this.timeout = 30 * 1000;
    this.developmentEnvironments = ['development', 'test'];
    this.consoleLogError = false;
  
    this.protocol = 'https';
    this.serviceHost =  process.env.AIRBRAKE_SERVER || 'api.airbrake.io';
    this.requestOptions = {};
    this.ignoredExceptions = [];
    this.exclude = [
      'type',
      'message',
      'arguments',
      'stack',
      'url',
      'session',
      'params',
      'component',
      'action',
      'domain',
      'domainEmitter',
      'domainBound',
      'ua'
    ];
  }
  
  Airbrake.PACKAGE = (function() {
    var json = fs.readFileSync(__dirname + '/../package.json', 'utf8');
    return JSON.parse(json);
  })();
  
  Airbrake.createClient = function(key, env) {
    var instance = new this();
    instance.key = key;
    instance.env = env || instance.env;
    return instance;
  };