/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./main.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./cfg/pop_menu.js":
/*!*************************!*\
  !*** ./cfg/pop_menu.js ***!
  \*************************/
/*! exports provided: pop */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"pop\", function() { return pop; });\nvar pop = {\n  pop_menu: function pop_menu(menu, x, y, scope) {\n    return new Promise(function (resolve, reject) {\n      var pop_id = new Date().getTime();\n      $('body').append(\"<div id=\\\"pop_\".concat(pop_id, \"\\\" style=\\\"position: fixed;top:0;left:0;bottom: 0;right: 0;\\\" @click=\\\"on_close\\\">\\n                <ul :style=\\\"{top:y,left:x}\\\" class=\\\"right-menu\\\">\\n                    <li v-for=\\\"action in menu\\\">\\n                        <span v-text=\\\"action.label\\\" @click=\\\"onclick(action)\\\"></span>\\n                    </li>\\n                </ul>\\n            </div>\"));\n      new Vue({\n        el: '#pop_' + pop_id,\n        data: function data() {\n          var childStore = new Vue();\n          childStore.vc = this;\n          return {\n            show: true,\n            menu: menu,\n            childStore: childStore,\n            x: x + 'px',\n            y: y + 'px',\n            scope: scope || {}\n          };\n        },\n        watch: {\n          show: function show(nv, ov) {\n            if (ov && !nv) {\n              $('#pop_' + pop_id).remove();\n            }\n          }\n        },\n        computed: {\n          mystyle: function mystyle() {\n            return {\n              top: this.y,\n              left: this.x\n            };\n          }\n        },\n        methods: {\n          onclick: function onclick(item) {\n            if (item.action) {\n              ex.eval(item.action, scope);\n            }\n          },\n          close: function close() {\n            this.show = false;\n          },\n          on_finish: function on_finish(e) {\n            this.show = false;\n            resolve(e);\n          },\n          on_close: function on_close() {\n            $('#pop_' + pop_id).remove();\n          }\n        }\n      });\n    });\n  },\n  prompt: function prompt() {\n    return new Promise(function (resolve, reject) {\n      layer.prompt(function (val, index) {\n        //layer.msg('得到了'+val);\n        resolve(val);\n        layer.close(index);\n      });\n    });\n  }\n};\n\n//# sourceURL=webpack:///./cfg/pop_menu.js?");

/***/ }),

/***/ "./main.js":
/*!*****************!*\
  !*** ./main.js ***!
  \*****************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _cfg_pop_menu__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./cfg/pop_menu */ \"./cfg/pop_menu.js\");\n\nex.assign(window.cfg, _cfg_pop_menu__WEBPACK_IMPORTED_MODULE_0__[\"pop\"]);\n\n//# sourceURL=webpack:///./main.js?");

/***/ })

/******/ });