const test = require("node:test");
const assert = require("node:assert/strict");

test("synthetic canary", () => {
  assert.equal(2 + 2, 4);
});
