var fs = require('fs-extra');
var fspath = require("path");
var gitTools = require("./git");


class Project {
    constructor(name, path) {
        this.name = name;
        this.path = path;
    }

    getFile(filePath, treeish) {
        if (treeish !== "_") {
            return gitTools.getFile(this.path, filePath, treeish);
        } else {
            return new Promise((resolve, reject) => {
                fs.readFile(fspath.join(this.path, filePath), "utf8", (err, data) => {
                    if (err) reject(err);
                    else resolve(data);
                });
            });
        }
    }
}

// Sample usage within an Express app
const app = express();
const projects = [new Project('ExampleProject', '/var/www/projects/ExampleProject')];

app.get('/file', (req, res) => {
    const { projectName, filePath, treeish } = req.query;

    const project = projects.find(p => p.name === projectName);
    if (!project) {
        return res.status(404).send('Project not found');
    }

    project.getFile(filePath, treeish)
        .then(data => res.send(`<pre>${data}</pre>`))
        .catch(err => res.status(500).send('Error reading file'));
});