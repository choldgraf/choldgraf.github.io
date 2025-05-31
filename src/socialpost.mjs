const socialPostDirective = {
  name: 'socialpost',
  doc: 'A placeholder to prevent the socialpost directive from throwing errors.',
  arg: { type: String, doc: 'The link for the social post' },
  options: {},
  run(data) {
    const postlink = data.arg;
    const size = data.options?.size || '500x200';
    const link = {
      "type": "link",
      "url": postlink,
      "children": [
        {
          "type": "text",
          "value": postlink,
        }
      ]
    };
    return [link];
  },
};

const plugin = { name: 'Social Post', directives: [socialPostDirective] };

export default plugin;
