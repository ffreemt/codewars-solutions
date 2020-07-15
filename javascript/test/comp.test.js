// const consola = require("consola");
const expect = require("chai").expect;
const sinon = require("sinon");
const assert = require("assert");

const comp = require("../comp");

describe("comp mocha test ", () => {
  context(" sanity ", () => {
    it("should pass ", () => {
      console.debug("\tln9> ddd1 ");
      const res = comp([], []);
      // expect(res).to.equal(true);
      // assert(sinon.match.truthy.test(res))
      assert.equal(res, true, " fail message")
    });
  });

  context(" null ", () => {
    it("should pass ", () => {
      console.debug("\tln17> ddd1 ");
      const res = comp(null, []);
      expect(res).to.equal(false);
      // sinon.assert(!res)
    });
  });

  context(" comp(a, b) ", () => {
    it("should pass ", () => {
      let a, b;
      a = [121, 144, 19, 161, 19, 144, 19, 11];
      b =  [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];
      console.debug("\tln20> a. b: ", a, b);
      const res = comp(a, b);
      expect(res).to.equal(true);
    });
  });

});