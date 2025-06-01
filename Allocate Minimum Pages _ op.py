<!DOCTYPE html>
<!-- saved from url=(0077)https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1 -->
<html lang="en" style="--vh: 6.95px;"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style id="ace-eclipse">.ace-eclipse .ace_gutter {background: #ebebeb;border-right: 1px solid rgb(159, 159, 159);color: rgb(136, 136, 136);}.ace-eclipse .ace_print-margin {width: 1px;background: #ebebeb;}.ace-eclipse {background-color: #FFFFFF;color: black;}.ace-eclipse .ace_fold {background-color: rgb(60, 76, 114);}.ace-eclipse .ace_cursor {color: black;}.ace-eclipse .ace_storage,.ace-eclipse .ace_keyword,.ace-eclipse .ace_variable {color: rgb(127, 0, 85);}.ace-eclipse .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-eclipse .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-eclipse .ace_function {color: rgb(60, 76, 114);}.ace-eclipse .ace_string {color: rgb(42, 0, 255);}.ace-eclipse .ace_comment {color: rgb(113, 150, 130);}.ace-eclipse .ace_comment.ace_doc {color: rgb(63, 95, 191);}.ace-eclipse .ace_comment.ace_doc.ace_tag {color: rgb(127, 159, 191);}.ace-eclipse .ace_constant.ace_numeric {color: darkblue;}.ace-eclipse .ace_tag {color: rgb(25, 118, 116);}.ace-eclipse .ace_type {color: rgb(127, 0, 127);}.ace-eclipse .ace_xml-pe {color: rgb(104, 104, 91);}.ace-eclipse .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-eclipse .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-eclipse .ace_meta.ace_tag {color:rgb(25, 118, 116);}.ace-eclipse .ace_invisible {color: #ddd;}.ace-eclipse .ace_entity.ace_other.ace_attribute-name {color:rgb(127, 0, 127);}.ace-eclipse .ace_marker-layer .ace_step {background: rgb(255, 255, 0);}.ace-eclipse .ace_active-line {background: rgb(232, 242, 254);}.ace-eclipse .ace_gutter-active-line {background-color : #DADADA;}.ace-eclipse .ace_marker-layer .ace_selected-word {border: 1px solid rgb(181, 213, 255);}.ace-eclipse .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-eclipse */</style><style id="ace-terminal-theme">.ace-terminal-theme .ace_gutter {background: #1a0005;color: steelblue}.ace-terminal-theme .ace_print-margin {width: 1px;background: #1a1a1a}.ace-terminal-theme {background-color: black;color: #DEDEDE}.ace-terminal-theme .ace_cursor {color: #9F9F9F}.ace-terminal-theme .ace_marker-layer .ace_selection {background: #424242}.ace-terminal-theme.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px black;}.ace-terminal-theme .ace_marker-layer .ace_step {background: rgb(0, 0, 0)}.ace-terminal-theme .ace_marker-layer .ace_bracket {background: #090;}.ace-terminal-theme .ace_marker-layer .ace_bracket-start {background: #090;}.ace-terminal-theme .ace_marker-layer .ace_bracket-unmatched {margin: -1px 0 0 -1px;border: 1px solid #900}.ace-terminal-theme .ace_marker-layer .ace_active-line {background: #2A2A2A}.ace-terminal-theme .ace_gutter-active-line {background-color: #2A112A}.ace-terminal-theme .ace_marker-layer .ace_selected-word {border: 1px solid #424242}.ace-terminal-theme .ace_invisible {color: #343434}.ace-terminal-theme .ace_keyword,.ace-terminal-theme .ace_meta,.ace-terminal-theme .ace_storage,.ace-terminal-theme .ace_storage.ace_type,.ace-terminal-theme .ace_support.ace_type {color: tomato}.ace-terminal-theme .ace_keyword.ace_operator {color: deeppink}.ace-terminal-theme .ace_constant.ace_character,.ace-terminal-theme .ace_constant.ace_language,.ace-terminal-theme .ace_constant.ace_numeric,.ace-terminal-theme .ace_keyword.ace_other.ace_unit,.ace-terminal-theme .ace_support.ace_constant,.ace-terminal-theme .ace_variable.ace_parameter {color: #E78C45}.ace-terminal-theme .ace_constant.ace_other {color: gold}.ace-terminal-theme .ace_invalid {color: yellow;background-color: red}.ace-terminal-theme .ace_invalid.ace_deprecated {color: #CED2CF;background-color: #B798BF}.ace-terminal-theme .ace_fold {background-color: #7AA6DA;border-color: #DEDEDE}.ace-terminal-theme .ace_entity.ace_name.ace_function,.ace-terminal-theme .ace_support.ace_function,.ace-terminal-theme .ace_variable {color: #7AA6DA}.ace-terminal-theme .ace_support.ace_class,.ace-terminal-theme .ace_support.ace_type {color: #E7C547}.ace-terminal-theme .ace_heading,.ace-terminal-theme .ace_string {color: #B9CA4A}.ace-terminal-theme .ace_entity.ace_name.ace_tag,.ace-terminal-theme .ace_entity.ace_other.ace_attribute-name,.ace-terminal-theme .ace_meta.ace_tag,.ace-terminal-theme .ace_string.ace_regexp,.ace-terminal-theme .ace_variable {color: #D54E53}.ace-terminal-theme .ace_comment {color: orangered}.ace-terminal-theme .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYLBWV/8PAAK4AYnhiq+xAAAAAElFTkSuQmCC) right repeat-y;}
/*# sourceURL=ace/css/ace-terminal-theme */</style><style id="ace-solarized-light">.ace-solarized-light .ace_gutter {background: #fbf1d3;color: #333}.ace-solarized-light .ace_print-margin {width: 1px;background: #e8e8e8}.ace-solarized-light {background-color: #FDF6E3;color: #586E75}.ace-solarized-light .ace_cursor {color: #000000}.ace-solarized-light .ace_marker-layer .ace_selection {background: rgba(7, 54, 67, 0.09)}.ace-solarized-light.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #FDF6E3;}.ace-solarized-light .ace_marker-layer .ace_step {background: rgb(255, 255, 0)}.ace-solarized-light .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgba(147, 161, 161, 0.50)}.ace-solarized-light .ace_marker-layer .ace_active-line {background: #EEE8D5}.ace-solarized-light .ace_gutter-active-line {background-color : #EDE5C1}.ace-solarized-light .ace_marker-layer .ace_selected-word {border: 1px solid #7f9390}.ace-solarized-light .ace_invisible {color: rgba(147, 161, 161, 0.50)}.ace-solarized-light .ace_keyword,.ace-solarized-light .ace_meta,.ace-solarized-light .ace_support.ace_class,.ace-solarized-light .ace_support.ace_type {color: #859900}.ace-solarized-light .ace_constant.ace_character,.ace-solarized-light .ace_constant.ace_other {color: #CB4B16}.ace-solarized-light .ace_constant.ace_language {color: #B58900}.ace-solarized-light .ace_constant.ace_numeric {color: #D33682}.ace-solarized-light .ace_fold {background-color: #268BD2;border-color: #586E75}.ace-solarized-light .ace_entity.ace_name.ace_function,.ace-solarized-light .ace_entity.ace_name.ace_tag,.ace-solarized-light .ace_support.ace_function,.ace-solarized-light .ace_variable,.ace-solarized-light .ace_variable.ace_language {color: #268BD2}.ace-solarized-light .ace_storage {color: #073642}.ace-solarized-light .ace_string {color: #2AA198}.ace-solarized-light .ace_string.ace_regexp {color: #D30102}.ace-solarized-light .ace_comment,.ace-solarized-light .ace_entity.ace_other.ace_attribute-name {color: #93A1A1}.ace-solarized-light .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHjy8NJ/AAjgA5fzQUmBAAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-solarized-light */</style><style id="ace-solarized-dark">.ace-solarized-dark .ace_gutter {background: #01313f;color: #d0edf7}.ace-solarized-dark .ace_print-margin {width: 1px;background: #33555E}.ace-solarized-dark {background-color: #002B36;color: #93A1A1}.ace-solarized-dark .ace_entity.ace_other.ace_attribute-name,.ace-solarized-dark .ace_storage {color: #93A1A1}.ace-solarized-dark .ace_cursor,.ace-solarized-dark .ace_string.ace_regexp {color: #D30102}.ace-solarized-dark .ace_marker-layer .ace_active-line,.ace-solarized-dark .ace_marker-layer .ace_selection {background: rgba(255, 255, 255, 0.1)}.ace-solarized-dark.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #002B36;}.ace-solarized-dark .ace_marker-layer .ace_step {background: rgb(102, 82, 0)}.ace-solarized-dark .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgba(147, 161, 161, 0.50)}.ace-solarized-dark .ace_gutter-active-line {background-color: #0d3440}.ace-solarized-dark .ace_marker-layer .ace_selected-word {border: 1px solid #073642}.ace-solarized-dark .ace_invisible {color: rgba(147, 161, 161, 0.50)}.ace-solarized-dark .ace_keyword,.ace-solarized-dark .ace_meta,.ace-solarized-dark .ace_support.ace_class,.ace-solarized-dark .ace_support.ace_type {color: #859900}.ace-solarized-dark .ace_constant.ace_character,.ace-solarized-dark .ace_constant.ace_other {color: #CB4B16}.ace-solarized-dark .ace_constant.ace_language {color: #B58900}.ace-solarized-dark .ace_constant.ace_numeric {color: #D33682}.ace-solarized-dark .ace_fold {background-color: #268BD2;border-color: #93A1A1}.ace-solarized-dark .ace_entity.ace_name.ace_function,.ace-solarized-dark .ace_entity.ace_name.ace_tag,.ace-solarized-dark .ace_support.ace_function,.ace-solarized-dark .ace_variable,.ace-solarized-dark .ace_variable.ace_language {color: #268BD2}.ace-solarized-dark .ace_string {color: #2AA198}.ace-solarized-dark .ace_comment {font-style: italic;color: #657B83}.ace-solarized-dark .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNg0Db1ZVCxc/sPAAd4AlUHlLenAAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-solarized-dark */</style><style id="ace-xcode">.ace-xcode .ace_gutter {background: #e8e8e8;color: #333}.ace-xcode .ace_print-margin {width: 1px;background: #e8e8e8}.ace-xcode {background-color: #FFFFFF;color: #000000}.ace-xcode .ace_cursor {color: #000000}.ace-xcode .ace_marker-layer .ace_selection {background: #B5D5FF}.ace-xcode.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #FFFFFF;}.ace-xcode .ace_marker-layer .ace_step {background: rgb(198, 219, 174)}.ace-xcode .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid #BFBFBF}.ace-xcode .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.071)}.ace-xcode .ace_gutter-active-line {background-color: rgba(0, 0, 0, 0.071)}.ace-xcode .ace_marker-layer .ace_selected-word {border: 1px solid #B5D5FF}.ace-xcode .ace_constant.ace_language,.ace-xcode .ace_keyword,.ace-xcode .ace_meta,.ace-xcode .ace_variable.ace_language {color: #C800A4}.ace-xcode .ace_invisible {color: #BFBFBF}.ace-xcode .ace_constant.ace_character,.ace-xcode .ace_constant.ace_other {color: #275A5E}.ace-xcode .ace_constant.ace_numeric {color: #3A00DC}.ace-xcode .ace_entity.ace_other.ace_attribute-name,.ace-xcode .ace_support.ace_constant,.ace-xcode .ace_support.ace_function {color: #450084}.ace-xcode .ace_fold {background-color: #C800A4;border-color: #000000}.ace-xcode .ace_entity.ace_name.ace_tag,.ace-xcode .ace_support.ace_class,.ace-xcode .ace_support.ace_type {color: #790EAD}.ace-xcode .ace_storage {color: #C900A4}.ace-xcode .ace_string {color: #DF0002}.ace-xcode .ace_comment {color: #008E00}.ace-xcode .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==) right repeat-y}
/*# sourceURL=ace/css/ace-xcode */</style><style id="ace-dracula">.ace-dracula .ace_gutter {background: #282a36;color: rgb(144,145,148)}.ace-dracula .ace_print-margin {width: 1px;background: #44475a}.ace-dracula {background-color: #282a36;color: #f8f8f2}.ace-dracula .ace_cursor {color: #f8f8f0}.ace-dracula .ace_marker-layer .ace_selection {background: #44475a}.ace-dracula.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #282a36;border-radius: 2px}.ace-dracula .ace_marker-layer .ace_step {background: rgb(198, 219, 174)}.ace-dracula .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid #a29709}.ace-dracula .ace_marker-layer .ace_active-line {background: #44475a}.ace-dracula .ace_gutter-active-line {background-color: #44475a}.ace-dracula .ace_marker-layer .ace_selected-word {box-shadow: 0px 0px 0px 1px #a29709;border-radius: 3px;}.ace-dracula .ace_fold {background-color: #50fa7b;border-color: #f8f8f2}.ace-dracula .ace_keyword {color: #ff79c6}.ace-dracula .ace_constant.ace_language {color: #bd93f9}.ace-dracula .ace_constant.ace_numeric {color: #bd93f9}.ace-dracula .ace_constant.ace_character {color: #bd93f9}.ace-dracula .ace_constant.ace_character.ace_escape {color: #ff79c6}.ace-dracula .ace_constant.ace_other {color: #bd93f9}.ace-dracula .ace_support.ace_function {color: #8be9fd}.ace-dracula .ace_support.ace_constant {color: #6be5fd}.ace-dracula .ace_support.ace_class {font-style: italic;color: #66d9ef}.ace-dracula .ace_support.ace_type {font-style: italic;color: #66d9ef}.ace-dracula .ace_storage {color: #ff79c6}.ace-dracula .ace_storage.ace_type {font-style: italic;color: #8be9fd}.ace-dracula .ace_invalid {color: #F8F8F0;background-color: #ff79c6}.ace-dracula .ace_invalid.ace_deprecated {color: #F8F8F0;background-color: #bd93f9}.ace-dracula .ace_string {color: #f1fa8c}.ace-dracula .ace_comment {color: #6272a4}.ace-dracula .ace_variable {color: #50fa7b}.ace-dracula .ace_variable.ace_parameter {font-style: italic;color: #ffb86c}.ace-dracula .ace_entity.ace_other.ace_attribute-name {color: #50fa7b}.ace-dracula .ace_entity.ace_name.ace_function {color: #50fa7b}.ace-dracula .ace_entity.ace_name.ace_tag {color: #ff79c6}.ace-dracula .ace_invisible {color: #626680;}.ace-dracula .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHB3d/8PAAOIAdULw8qMAAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-dracula */</style><style id="ace-twilight">.ace-twilight .ace_gutter {background: #232323;color: #E2E2E2}.ace-twilight .ace_print-margin {width: 1px;background: #232323}.ace-twilight {background-color: #141414;color: #F8F8F8}.ace-twilight .ace_cursor {color: #A7A7A7}.ace-twilight .ace_marker-layer .ace_selection {background: rgba(221, 240, 255, 0.20)}.ace-twilight.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #141414;}.ace-twilight .ace_marker-layer .ace_step {background: rgb(102, 82, 0)}.ace-twilight .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgba(255, 255, 255, 0.25)}.ace-twilight .ace_marker-layer .ace_active-line {background: rgba(255, 255, 255, 0.031)}.ace-twilight .ace_gutter-active-line {background-color: rgba(255, 255, 255, 0.031)}.ace-twilight .ace_marker-layer .ace_selected-word {border: 1px solid rgba(221, 240, 255, 0.20)}.ace-twilight .ace_invisible {color: rgba(255, 255, 255, 0.25)}.ace-twilight .ace_keyword,.ace-twilight .ace_meta {color: #CDA869}.ace-twilight .ace_constant,.ace-twilight .ace_constant.ace_character,.ace-twilight .ace_constant.ace_character.ace_escape,.ace-twilight .ace_constant.ace_other,.ace-twilight .ace_heading,.ace-twilight .ace_markup.ace_heading,.ace-twilight .ace_support.ace_constant {color: #CF6A4C}.ace-twilight .ace_invalid.ace_illegal {color: #F8F8F8;background-color: rgba(86, 45, 86, 0.75)}.ace-twilight .ace_invalid.ace_deprecated {text-decoration: underline;font-style: italic;color: #D2A8A1}.ace-twilight .ace_support {color: #9B859D}.ace-twilight .ace_fold {background-color: #AC885B;border-color: #F8F8F8}.ace-twilight .ace_support.ace_function {color: #DAD085}.ace-twilight .ace_list,.ace-twilight .ace_markup.ace_list,.ace-twilight .ace_storage {color: #F9EE98}.ace-twilight .ace_entity.ace_name.ace_function,.ace-twilight .ace_meta.ace_tag {color: #AC885B}.ace-twilight .ace_string {color: #8F9D6A}.ace-twilight .ace_string.ace_regexp {color: #E9C062}.ace-twilight .ace_comment {font-style: italic;color: #5F5A60}.ace-twilight .ace_variable {color: #7587A6}.ace-twilight .ace_xml-pe {color: #494949}.ace-twilight .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWMQERFpYLC1tf0PAAgOAnPnhxyiAAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-twilight */</style><style id="ace-kuroir">.ace-kuroir .ace_gutter {background: #e8e8e8;color: #333;}.ace-kuroir .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-kuroir {background-color: #E8E9E8;color: #363636;}.ace-kuroir .ace_cursor {color: #202020;}.ace-kuroir .ace_marker-layer .ace_selection {background: rgba(245, 170, 0, 0.57);}.ace-kuroir.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #E8E9E8;}.ace-kuroir .ace_marker-layer .ace_step {background: rgb(198, 219, 174);}.ace-kuroir .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgba(0, 0, 0, 0.29);}.ace-kuroir .ace_marker-layer .ace_active-line {background: rgba(203, 220, 47, 0.22);}.ace-kuroir .ace_gutter-active-line {background-color: rgba(203, 220, 47, 0.22);}.ace-kuroir .ace_marker-layer .ace_selected-word {border: 1px solid rgba(245, 170, 0, 0.57);}.ace-kuroir .ace_invisible {color: #BFBFBF}.ace-kuroir .ace_fold {border-color: #363636;}.ace-kuroir .ace_constant{color:#CD6839;}.ace-kuroir .ace_constant.ace_numeric{color:#9A5925;}.ace-kuroir .ace_support{color:#104E8B;}.ace-kuroir .ace_support.ace_function{color:#005273;}.ace-kuroir .ace_support.ace_constant{color:#CF6A4C;}.ace-kuroir .ace_storage{color:#A52A2A;}.ace-kuroir .ace_invalid.ace_illegal{color:#FD1224;background-color:rgba(255, 6, 0, 0.15);}.ace-kuroir .ace_invalid.ace_deprecated{text-decoration:underline;font-style:italic;color:#FD1732;background-color:#E8E9E8;}.ace-kuroir .ace_string{color:#639300;}.ace-kuroir .ace_string.ace_regexp{color:#417E00;background-color:#C9D4BE;}.ace-kuroir .ace_comment{color:rgba(148, 148, 148, 0.91);background-color:rgba(220, 220, 220, 0.56);}.ace-kuroir .ace_variable{color:#009ACD;}.ace-kuroir .ace_meta.ace_tag{color:#005273;}.ace-kuroir .ace_markup.ace_heading{color:#B8012D;background-color:rgba(191, 97, 51, 0.051);}.ace-kuroir .ace_markup.ace_list{color:#8F5B26;}
/*# sourceURL=ace/css/ace-kuroir */</style><style id="ace-tomorrow">.ace-tomorrow .ace_gutter {background: #f6f6f6;color: #4D4D4C}.ace-tomorrow .ace_print-margin {width: 1px;background: #f6f6f6}.ace-tomorrow {background-color: #FFFFFF;color: #4D4D4C}.ace-tomorrow .ace_cursor {color: #AEAFAD}.ace-tomorrow .ace_marker-layer .ace_selection {background: #D6D6D6}.ace-tomorrow.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #FFFFFF;}.ace-tomorrow .ace_marker-layer .ace_step {background: rgb(255, 255, 0)}.ace-tomorrow .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid #D1D1D1}.ace-tomorrow .ace_marker-layer .ace_active-line {background: #EFEFEF}.ace-tomorrow .ace_gutter-active-line {background-color : #dcdcdc}.ace-tomorrow .ace_marker-layer .ace_selected-word {border: 1px solid #D6D6D6}.ace-tomorrow .ace_invisible {color: #D1D1D1}.ace-tomorrow .ace_keyword,.ace-tomorrow .ace_meta,.ace-tomorrow .ace_storage,.ace-tomorrow .ace_storage.ace_type,.ace-tomorrow .ace_support.ace_type {color: #8959A8}.ace-tomorrow .ace_keyword.ace_operator {color: #3E999F}.ace-tomorrow .ace_constant.ace_character,.ace-tomorrow .ace_constant.ace_language,.ace-tomorrow .ace_constant.ace_numeric,.ace-tomorrow .ace_keyword.ace_other.ace_unit,.ace-tomorrow .ace_support.ace_constant,.ace-tomorrow .ace_variable.ace_parameter {color: #F5871F}.ace-tomorrow .ace_constant.ace_other {color: #666969}.ace-tomorrow .ace_invalid {color: #FFFFFF;background-color: #C82829}.ace-tomorrow .ace_invalid.ace_deprecated {color: #FFFFFF;background-color: #8959A8}.ace-tomorrow .ace_fold {background-color: #4271AE;border-color: #4D4D4C}.ace-tomorrow .ace_entity.ace_name.ace_function,.ace-tomorrow .ace_support.ace_function,.ace-tomorrow .ace_variable {color: #4271AE}.ace-tomorrow .ace_support.ace_class,.ace-tomorrow .ace_support.ace_type {color: #C99E00}.ace-tomorrow .ace_heading,.ace-tomorrow .ace_markup.ace_heading,.ace-tomorrow .ace_string {color: #718C00}.ace-tomorrow .ace_entity.ace_name.ace_tag,.ace-tomorrow .ace_entity.ace_other.ace_attribute-name,.ace-tomorrow .ace_meta.ace_tag,.ace-tomorrow .ace_string.ace_regexp,.ace-tomorrow .ace_variable {color: #C82829}.ace-tomorrow .ace_comment {color: #8E908C}.ace-tomorrow .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bdu3f/BwAlfgctduB85QAAAABJRU5ErkJggg==) right repeat-y}
/*# sourceURL=ace/css/ace-tomorrow */</style><style id="ace-github">.ace-github .ace_gutter {background: #e8e8e8;color: #AAA;}.ace-github  {background: #fff;color: #000;}.ace-github .ace_keyword {font-weight: bold;}.ace-github .ace_string {color: #D14;}.ace-github .ace_variable.ace_class {color: teal;}.ace-github .ace_constant.ace_numeric {color: #099;}.ace-github .ace_constant.ace_buildin {color: #0086B3;}.ace-github .ace_support.ace_function {color: #0086B3;}.ace-github .ace_comment {color: #998;font-style: italic;}.ace-github .ace_variable.ace_language  {color: #0086B3;}.ace-github .ace_paren {font-weight: bold;}.ace-github .ace_boolean {font-weight: bold;}.ace-github .ace_string.ace_regexp {color: #009926;font-weight: normal;}.ace-github .ace_variable.ace_instance {color: teal;}.ace-github .ace_constant.ace_language {font-weight: bold;}.ace-github .ace_cursor {color: black;}.ace-github.ace_focus .ace_marker-layer .ace_active-line {background: rgb(255, 255, 204);}.ace-github .ace_marker-layer .ace_active-line {background: rgb(245, 245, 245);}.ace-github .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-github.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-github.ace_nobold .ace_line > span {font-weight: normal !important;}.ace-github .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-github .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-github .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-github .ace_gutter-active-line {background-color : rgba(0, 0, 0, 0.07);}.ace-github .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-github .ace_invisible {color: #BFBFBF}.ace-github .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-github .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-github */</style><style id="ace-monokai">.ace-monokai .ace_gutter {background: #2F3129;color: #8F908A}.ace-monokai .ace_print-margin {width: 1px;background: #555651}.ace-monokai {background-color: #272822;color: #F8F8F2}.ace-monokai .ace_cursor {color: #F8F8F0}.ace-monokai .ace_marker-layer .ace_selection {background: #49483E}.ace-monokai.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #272822;}.ace-monokai .ace_marker-layer .ace_step {background: rgb(102, 82, 0)}.ace-monokai .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid #49483E}.ace-monokai .ace_marker-layer .ace_active-line {background: #202020}.ace-monokai .ace_gutter-active-line {background-color: #272727}.ace-monokai .ace_marker-layer .ace_selected-word {border: 1px solid #49483E}.ace-monokai .ace_invisible {color: #52524d}.ace-monokai .ace_entity.ace_name.ace_tag,.ace-monokai .ace_keyword,.ace-monokai .ace_meta.ace_tag,.ace-monokai .ace_storage {color: #F92672}.ace-monokai .ace_punctuation,.ace-monokai .ace_punctuation.ace_tag {color: #fff}.ace-monokai .ace_constant.ace_character,.ace-monokai .ace_constant.ace_language,.ace-monokai .ace_constant.ace_numeric,.ace-monokai .ace_constant.ace_other {color: #AE81FF}.ace-monokai .ace_invalid {color: #F8F8F0;background-color: #F92672}.ace-monokai .ace_invalid.ace_deprecated {color: #F8F8F0;background-color: #AE81FF}.ace-monokai .ace_support.ace_constant,.ace-monokai .ace_support.ace_function {color: #66D9EF}.ace-monokai .ace_fold {background-color: #A6E22E;border-color: #F8F8F2}.ace-monokai .ace_storage.ace_type,.ace-monokai .ace_support.ace_class,.ace-monokai .ace_support.ace_type {font-style: italic;color: #66D9EF}.ace-monokai .ace_entity.ace_name.ace_function,.ace-monokai .ace_entity.ace_other,.ace-monokai .ace_entity.ace_other.ace_attribute-name,.ace-monokai .ace_variable {color: #A6E22E}.ace-monokai .ace_variable.ace_parameter {font-style: italic;color: #FD971F}.ace-monokai .ace_string {color: #E6DB74}.ace-monokai .ace_comment {color: #75715E}.ace-monokai .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWPQ0FD0ZXBzd/wPAAjVAoxeSgNeAAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-monokai */</style><style id="ace_searchbox">.ace_search {background-color: #ddd;color: #666;border: 1px solid #cbcbcb;border-top: 0 none;overflow: hidden;margin: 0;padding: 4px 6px 0 4px;position: absolute;top: 0;z-index: 99;white-space: normal;}.ace_search.left {border-left: 0 none;border-radius: 0px 0px 5px 0px;left: 0;}.ace_search.right {border-radius: 0px 0px 0px 5px;border-right: 0 none;right: 0;}.ace_search_form, .ace_replace_form {margin: 0 20px 4px 0;overflow: hidden;line-height: 1.9;}.ace_replace_form {margin-right: 0;}.ace_search_form.ace_nomatch {outline: 1px solid red;}.ace_search_field {border-radius: 3px 0 0 3px;background-color: white;color: black;border: 1px solid #cbcbcb;border-right: 0 none;outline: 0;padding: 0;font-size: inherit;margin: 0;line-height: inherit;padding: 0 6px;min-width: 17em;vertical-align: top;min-height: 1.8em;box-sizing: content-box;}.ace_searchbtn {border: 1px solid #cbcbcb;line-height: inherit;display: inline-block;padding: 0 6px;background: #fff;border-right: 0 none;border-left: 1px solid #dcdcdc;cursor: pointer;margin: 0;position: relative;color: #666;}.ace_searchbtn:last-child {border-radius: 0 3px 3px 0;border-right: 1px solid #cbcbcb;}.ace_searchbtn:disabled {background: none;cursor: default;}.ace_searchbtn:hover {background-color: #eef1f6;}.ace_searchbtn.prev, .ace_searchbtn.next {padding: 0px 0.7em}.ace_searchbtn.prev:after, .ace_searchbtn.next:after {content: "";border: solid 2px #888;width: 0.5em;height: 0.5em;border-width:  2px 0 0 2px;display:inline-block;transform: rotate(-45deg);}.ace_searchbtn.next:after {border-width: 0 2px 2px 0 ;}.ace_searchbtn_close {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAcCAYAAABRVo5BAAAAZ0lEQVR42u2SUQrAMAhDvazn8OjZBilCkYVVxiis8H4CT0VrAJb4WHT3C5xU2a2IQZXJjiQIRMdkEoJ5Q2yMqpfDIo+XY4k6h+YXOyKqTIj5REaxloNAd0xiKmAtsTHqW8sR2W5f7gCu5nWFUpVjZwAAAABJRU5ErkJggg==) no-repeat 50% 0;border-radius: 50%;border: 0 none;color: #656565;cursor: pointer;font: 16px/16px Arial;padding: 0;height: 14px;width: 14px;top: 9px;right: 7px;position: absolute;}.ace_searchbtn_close:hover {background-color: #656565;background-position: 50% 100%;color: white;}.ace_button {margin-left: 2px;cursor: pointer;-webkit-user-select: none;-moz-user-select: none;-o-user-select: none;-ms-user-select: none;user-select: none;overflow: hidden;opacity: 0.7;border: 1px solid rgba(100,100,100,0.23);padding: 1px;box-sizing:    border-box!important;color: black;}.ace_button:hover {background-color: #eee;opacity:1;}.ace_button:active {background-color: #ddd;}.ace_button.checked {border-color: #3399ff;opacity:1;}.ace_search_options{margin-bottom: 3px;text-align: right;-webkit-user-select: none;-moz-user-select: none;-o-user-select: none;-ms-user-select: none;user-select: none;clear: both;}.ace_search_counter {float: left;font-family: arial;padding: 0 8px;}
/*# sourceURL=ace/css/ace_searchbox */</style><style id="error_marker.css">    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }
/*# sourceURL=ace/css/error_marker.css */</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;padding: 0;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}
/*# sourceURL=ace/css/ace_editor.css */</style><link rel="canonical" href="https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1"><link href="./Allocate Minimum Pages _ op_files/semantic.min.css" rel="stylesheet"><link rel="icon" href="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_favicon.png" type="image/x-icon"><meta name="keywords" content="programming, coding, online, code online, online judge, practice, run code, test, expected outcome, programming competition, programming contest, online programming, online computer programming, hackathon"><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes"><title>Allocate Minimum Pages | Practice | GeeksforGeeks </title><meta name="description" content="You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student"><meta property="og:title" content="Allocate Minimum Pages | Practice | GeeksforGeeks "><meta property="og:description" content="You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student"><meta property="og:image" content="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_200x200-min.png"><meta property="og:image:alt" content="GeeksforGeeks"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="200"><meta property="og:image:height" content="200"><meta property="twitter:card" content="summary_large_image"><meta property="twitter:title" content="Allocate Minimum Pages | Practice | GeeksforGeeks "><meta property="twitter:description" content="You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student"><meta property="twitter:image" content="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_200x200-min.png"><meta name="next-head-count" content="20"><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/insight.min.js.download"></script><script async="" src="./Allocate Minimum Pages _ op_files/283011338"></script><script async="" src="./Allocate Minimum Pages _ op_files/clarity.js.download"></script><script async="" src="./Allocate Minimum Pages _ op_files/uwt.js.download"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/bat.js.download"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/qevents.js.download"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/insight.min.js.download"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/js"></script><script src="./Allocate Minimum Pages _ op_files/2320390688070878" async=""></script><script src="./Allocate Minimum Pages _ op_files/sdk.js.download" async="" crossorigin="anonymous"></script><script async="" src="./Allocate Minimum Pages _ op_files/ayq955frd2"></script><script id="facebook-jssdk" src="./Allocate Minimum Pages _ op_files/sdk(1).js.download"></script><script async="" src="./Allocate Minimum Pages _ op_files/fbevents.js.download"></script><script async="" src="./Allocate Minimum Pages _ op_files/gtm.js.download"></script><script type="application/ld+json">{"@context":"http://schema.org","@type":"Organization","name":"GeeksforGeeks","url":"https://www.geeksforgeeks.org/","logo":"https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200817185016/gfg_complete_logo_2x-min.png","description":"A computer science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.","founder":[{"@type":"Person","name":"Sandeep Jain","url":"https://in.linkedin.com/in/sandeep-jain-b3940815"}],"sameAs":["https://www.facebook.com/geeksforgeeks.org/","https://twitter.com/geeksforgeeks","https://www.linkedin.com/company/1299009","https://www.youtube.com/geeksforgeeksvideos/"]}</script><link rel="preconnect" href="https://fonts.googleapis.com/"><link rel="preconnect" href="https://fonts.gstatic.com/"><link rel="preconnect" href="https://assets.geeksforgeeks.org/"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wIaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wsaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wMaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wwaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wAaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3wEaZfrc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/sourcesans3/v15/nwpStKy2OAdR1K-IwhWudF-R3w8aZQ.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/nunito/v26/XRXV3I6Li01BKofIOOaBXso.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/nunito/v26/XRXV3I6Li01BKofIMeaBXso.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/nunito/v26/XRXV3I6Li01BKofIOuaBXso.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/nunito/v26/XRXV3I6Li01BKofIO-aBXso.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/nunito/v26/XRXV3I6Li01BKofINeaB.woff2" as="font"><link rel="preload" href="https://assets.geeksforgeeks.org/static-editor/static/fonts/4dd591d8-4168-4263-b05b-7183ddaff1f4.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/lato/v24/S6u9w4BMUTPHh6UVSwiPGQ.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/lato/v24/S6u9w4BMUTPHh6UVSwiPGQ3q5d0.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/lato/v24/S6uyw4BMUTPHjx4wXiWtFCc.woff2" as="font"><link rel="preload" href="https://fonts.gstatic.com/s/lato/v24/S6uyw4BMUTPHjx4wXg.woff2" as="font"><link rel="preload" href="./Allocate Minimum Pages _ op_files/06d7ea1ef616e4bd.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/06d7ea1ef616e4bd.css" data-n-g=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/afd2ee21c00c924b.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/afd2ee21c00c924b.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/af5c5de7f44199f3.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/af5c5de7f44199f3.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/45083469add4caeb.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/45083469add4caeb.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/5d5a3b69eb5e6a17.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/5d5a3b69eb5e6a17.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/dea578a0b59997ac.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/dea578a0b59997ac.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/62baac51616b0ad4.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/62baac51616b0ad4.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/d87a706bb1562504.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/d87a706bb1562504.css" data-n-p=""><link rel="preload" href="./Allocate Minimum Pages _ op_files/bac5f0452a6b1968.css" as="style"><link rel="stylesheet" href="./Allocate Minimum Pages _ op_files/bac5f0452a6b1968.css"><noscript data-n-css=""></noscript><script defer="" nomodule="" src="./Allocate Minimum Pages _ op_files/polyfills-c67a75d1b6f99dc8.js.download"></script><script defer="" src="./Allocate Minimum Pages _ op_files/88040-aad6276d8640d5a3.js.download"></script><script defer="" src="./Allocate Minimum Pages _ op_files/83819.cd8b176640d23284.js.download"></script><script src="./Allocate Minimum Pages _ op_files/webpack-bb8750e11f096a5f.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/framework-932302aca1fc094d.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/main-77c66fcba07f33c0.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/_app-2503fa4e29a1880d.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/29107295-f5d3d9a71e7e292a.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/39138-08d6a077cfd9784c.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/60416-1fa73b554bc05def.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/43041-2c5e84032aa7f226.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/25675-ce1390d539636e49.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/78485-35c0668a5c623f09.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/96150-17ab063c79de610a.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/81733-b4c462f862132212.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/79750-ae35d9b56c543f3c.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/83465-9b84fd1f96f171b6.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/62002-ea6e593ab1b9d1b6.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/35080-4c441e811a506e07.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/24079-337a0a1272177ef6.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/80260-a8cb17f25a2278e3.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/47019-f4c571614892a99a.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/97578-83ea5a2476277330.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/59079-a7b1009862f4b3e6.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/11354-98be061f3fd675f7.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/23313-7bd0ebab9d34ab68.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/60420-458727421e1e6e15.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/86708-4632ccb29af9d63b.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/19898-4cc07806b0eb99ce.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/61771-49dbfdc8cd637697.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/12205-593a71c3c5c4624b.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/[probType]-4b0ab62ed3c70752.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/_buildManifest.js.download" defer=""></script><script src="./Allocate Minimum Pages _ op_files/_ssgManifest.js.download" defer=""></script><style id="__jsx-c095eb98ac24c0d7">body{overflow:hidden}@media(max-width:1024px){body{overflow:auto}}</style><script defer="" src="./Allocate Minimum Pages _ op_files/js(1)"></script><script defer="" src="./Allocate Minimum Pages _ op_files/js(2)"></script><script defer="">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-TH3MQN4')</script><script defer="">window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'AW-796001856');</script><script defer="">!function(f,b,e,v,n,t,s)
        {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
        n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)}(window, document,'script',
        'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', '2320390688070878');
        fbq('track', 'PageView');</script><script defer="">window.fbAsyncInit = function() {
            FB.init({
              appId      : '534961220012939',
              xfbml      : true,
              version    : 'v2.5'
            });
        };
        (function(d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) {return;}
            js = d.createElement(s); js.id = id;
            js.src = "//connect.facebook.net/en_US/sdk.js";
            fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));</script><script defer="">(function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "ayq955frd2")</script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/f.txt"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/f(1).txt"></script><script type="text/javascript" async="" src="./Allocate Minimum Pages _ op_files/f(2).txt"></script><script src="./Allocate Minimum Pages _ op_files/283011338.js.download" type="text/javascript" async="" data-ueto="ueto_c38faca0d7"></script><style type="text/css" data-fbcssmodules="css:fb.css.base css:fb.css.dialog css:fb.css.iframewidget">.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0px;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:'lucida grande', tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset>div{overflow:hidden}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0px;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:'lucida grande', tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset>div{overflow:hidden}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_dialog{background:rgba(82,82,82,.7);position:absolute;top:-10000px;z-index:10001}.fb_dialog_advanced{border-radius:8px;padding:10px}.fb_dialog_content{background:#fff;color:#373737}.fb_dialog_close_icon{background:url(https://connect.facebook.net/rsrc.php/v4/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 0 transparent;cursor:pointer;display:block;height:15px;position:absolute;right:18px;top:17px;width:15px}.fb_dialog_mobile .fb_dialog_close_icon{left:5px;right:auto;top:5px}.fb_dialog_padding{background-color:transparent;position:absolute;width:1px;z-index:-1}.fb_dialog_close_icon:hover{background:url(https://connect.facebook.net/rsrc.php/v4/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -15px transparent}.fb_dialog_close_icon:active{background:url(https://connect.facebook.net/rsrc.php/v4/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -30px transparent}.fb_dialog_iframe{line-height:0}.fb_dialog_content .dialog_title{background:#6d84b4;border:1px solid #365899;color:#fff;font-size:14px;font-weight:bold;margin:0}.fb_dialog_content .dialog_title>span{background:url(https://connect.facebook.net/rsrc.php/v4/yd/r/Cou7n-nqK52.gif) no-repeat 5px 50%;float:left;padding:5px 0 7px 26px}body.fb_hidden{height:100%;left:0px;margin:0px;overflow:visible;position:absolute;top:-10000px;transform:none;width:100%}.fb_dialog.fb_dialog_mobile.loading{background:url(https://connect.facebook.net/rsrc.php/v4/ya/r/3rhSv5V8j3o.gif) white no-repeat 50% 50%;min-height:100%;min-width:100%;overflow:hidden;position:absolute;top:0;z-index:10001}.fb_dialog.fb_dialog_mobile.loading.centered{background:none;height:auto;min-height:initial;min-width:initial;width:auto}.fb_dialog.fb_dialog_mobile.loading.centered #fb_dialog_loader_spinner{width:100%}.fb_dialog.fb_dialog_mobile.loading.centered .fb_dialog_content{background:none}.loading.centered #fb_dialog_loader_close{clear:both;color:white;display:block;font-size:18px;padding-top:20px}#fb-root #fb_dialog_ipad_overlay{background:rgba(0,0,0,.4);bottom:0;left:0;min-height:100%;position:absolute;right:0;top:0;width:100%;z-index:10000}#fb-root #fb_dialog_ipad_overlay.hidden{display:none}.fb_dialog.fb_dialog_mobile.loading iframe{visibility:hidden}.fb_dialog_mobile .fb_dialog_iframe{position:sticky;top:0}.fb_dialog_content .dialog_header{background:linear-gradient(from(#738aba), to(#2c4987));border-bottom:1px solid;border-color:#043b87;box-shadow:white 0px 1px 1px -1px inset;color:#fff;font:bold 14px Helvetica, sans-serif;text-overflow:ellipsis;text-shadow:rgba(0,30,84,.296875) 0px -1px 0px;vertical-align:middle;white-space:nowrap}.fb_dialog_content .dialog_header table{height:43px;width:100%}.fb_dialog_content .dialog_header td.header_left{font-size:12px;padding-left:5px;vertical-align:middle;width:60px}.fb_dialog_content .dialog_header td.header_right{font-size:12px;padding-right:5px;vertical-align:middle;width:60px}.fb_dialog_content .touchable_button{background:linear-gradient(from(#4267b2), to(#2a4887));background-clip:padding-box;border:1px solid #29487d;border-radius:3px;display:inline-block;line-height:18px;margin-top:3px;max-width:85px;padding:4px 12px;position:relative}.fb_dialog_content .dialog_header .touchable_button input{background:none;border:none;color:white;font:bold 12px Helvetica, sans-serif;margin:2px -12px;padding:2px 6px 3px 6px;text-shadow:rgba(0,30,84,.296875) 0px -1px 0px}.fb_dialog_content .dialog_header .header_center{color:#fff;font-size:16px;font-weight:bold;line-height:18px;text-align:center;vertical-align:middle}.fb_dialog_content .dialog_content{background:url(https://connect.facebook.net/rsrc.php/v4/y9/r/jKEcVPZFk-2.gif) no-repeat 50% 50%;border:1px solid #4a4a4a;border-bottom:0;border-top:0;height:150px}.fb_dialog_content .dialog_footer{background:#f5f6f7;border:1px solid #4a4a4a;border-top-color:#ccc;height:40px}#fb_dialog_loader_close{float:left}.fb_dialog.fb_dialog_mobile .fb_dialog_close_icon{visibility:hidden}#fb_dialog_loader_spinner{animation:rotateSpinner 1.2s linear infinite;background-color:transparent;background-image:url(https://connect.facebook.net/rsrc.php/v4/yD/r/t-wz8gw1xG1.png);background-position:50% 50%;background-repeat:no-repeat;height:24px;width:24px}@keyframes rotateSpinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.fb_iframe_widget{display:inline-block;position:relative}.fb_iframe_widget span{display:inline-block;position:relative;text-align:justify}.fb_iframe_widget iframe{position:absolute}.fb_iframe_widget_fluid_desktop,.fb_iframe_widget_fluid_desktop span,.fb_iframe_widget_fluid_desktop iframe{max-width:100%}.fb_iframe_widget_fluid_desktop iframe{min-width:220px;position:relative}.fb_iframe_widget_lift{z-index:1}.fb_iframe_widget_fluid{display:inline}.fb_iframe_widget_fluid span{width:100%}</style><style>:root {
  --toastify-color-light: #fff;
  --toastify-color-dark: #121212;
  --toastify-color-info: #3498db;
  --toastify-color-success: #07bc0c;
  --toastify-color-warning: #f1c40f;
  --toastify-color-error: #e74c3c;
  --toastify-color-transparent: rgba(255, 255, 255, 0.7);
  --toastify-icon-color-info: var(--toastify-color-info);
  --toastify-icon-color-success: var(--toastify-color-success);
  --toastify-icon-color-warning: var(--toastify-color-warning);
  --toastify-icon-color-error: var(--toastify-color-error);
  --toastify-toast-width: 320px;
  --toastify-toast-background: #fff;
  --toastify-toast-min-height: 64px;
  --toastify-toast-max-height: 800px;
  --toastify-font-family: sans-serif;
  --toastify-z-index: 9999;
  --toastify-text-color-light: #757575;
  --toastify-text-color-dark: #fff;
  --toastify-text-color-info: #fff;
  --toastify-text-color-success: #fff;
  --toastify-text-color-warning: #fff;
  --toastify-text-color-error: #fff;
  --toastify-spinner-color: #616161;
  --toastify-spinner-color-empty-area: #e0e0e0;
  --toastify-color-progress-light: linear-gradient(
    to right,
    #4cd964,
    #5ac8fa,
    #007aff,
    #34aadc,
    #5856d6,
    #ff2d55
  );
  --toastify-color-progress-dark: #bb86fc;
  --toastify-color-progress-info: var(--toastify-color-info);
  --toastify-color-progress-success: var(--toastify-color-success);
  --toastify-color-progress-warning: var(--toastify-color-warning);
  --toastify-color-progress-error: var(--toastify-color-error);
}

.Toastify__toast-container {
  z-index: var(--toastify-z-index);
  -webkit-transform: translate3d(0, 0, var(--toastify-z-index) px);
  position: fixed;
  padding: 4px;
  width: var(--toastify-toast-width);
  box-sizing: border-box;
  color: #fff;
}
.Toastify__toast-container--top-left {
  top: 1em;
  left: 1em;
}
.Toastify__toast-container--top-center {
  top: 1em;
  left: 50%;
  transform: translateX(-50%);
}
.Toastify__toast-container--top-right {
  top: 1em;
  right: 1em;
}
.Toastify__toast-container--bottom-left {
  bottom: 1em;
  left: 1em;
}
.Toastify__toast-container--bottom-center {
  bottom: 1em;
  left: 50%;
  transform: translateX(-50%);
}
.Toastify__toast-container--bottom-right {
  bottom: 1em;
  right: 1em;
}

@media only screen and (max-width : 480px) {
  .Toastify__toast-container {
    width: 100vw;
    padding: 0;
    left: 0;
    margin: 0;
  }
  .Toastify__toast-container--top-left, .Toastify__toast-container--top-center, .Toastify__toast-container--top-right {
    top: 0;
    transform: translateX(0);
  }
  .Toastify__toast-container--bottom-left, .Toastify__toast-container--bottom-center, .Toastify__toast-container--bottom-right {
    bottom: 0;
    transform: translateX(0);
  }
  .Toastify__toast-container--rtl {
    right: 0;
    left: initial;
  }
}
.Toastify__toast {
  position: relative;
  min-height: var(--toastify-toast-min-height);
  box-sizing: border-box;
  margin-bottom: 1rem;
  padding: 8px;
  border-radius: 4px;
  box-shadow: 0 1px 10px 0 rgba(0, 0, 0, 0.1), 0 2px 15px 0 rgba(0, 0, 0, 0.05);
  display: -ms-flexbox;
  display: flex;
  -ms-flex-pack: justify;
      justify-content: space-between;
  max-height: var(--toastify-toast-max-height);
  overflow: hidden;
  font-family: var(--toastify-font-family);
  cursor: pointer;
  direction: ltr;
}
.Toastify__toast--rtl {
  direction: rtl;
}
.Toastify__toast-body {
  margin: auto 0;
  -ms-flex: 1 1 auto;
      flex: 1 1 auto;
  padding: 6px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
      align-items: center;
}
.Toastify__toast-body > div:last-child {
  -ms-flex: 1;
      flex: 1;
}
.Toastify__toast-icon {
  -webkit-margin-end: 10px;
          margin-inline-end: 10px;
  width: 20px;
  -ms-flex-negative: 0;
      flex-shrink: 0;
  display: -ms-flexbox;
  display: flex;
}

.Toastify--animate {
  animation-fill-mode: both;
  animation-duration: 0.7s;
}

.Toastify--animate-icon {
  animation-fill-mode: both;
  animation-duration: 0.3s;
}

@media only screen and (max-width : 480px) {
  .Toastify__toast {
    margin-bottom: 0;
    border-radius: 0;
  }
}
.Toastify__toast-theme--dark {
  background: var(--toastify-color-dark);
  color: var(--toastify-text-color-dark);
}
.Toastify__toast-theme--light {
  background: var(--toastify-color-light);
  color: var(--toastify-text-color-light);
}
.Toastify__toast-theme--colored.Toastify__toast--default {
  background: var(--toastify-color-light);
  color: var(--toastify-text-color-light);
}
.Toastify__toast-theme--colored.Toastify__toast--info {
  color: var(--toastify-text-color-info);
  background: var(--toastify-color-info);
}
.Toastify__toast-theme--colored.Toastify__toast--success {
  color: var(--toastify-text-color-success);
  background: var(--toastify-color-success);
}
.Toastify__toast-theme--colored.Toastify__toast--warning {
  color: var(--toastify-text-color-warning);
  background: var(--toastify-color-warning);
}
.Toastify__toast-theme--colored.Toastify__toast--error {
  color: var(--toastify-text-color-error);
  background: var(--toastify-color-error);
}

.Toastify__progress-bar-theme--light {
  background: var(--toastify-color-progress-light);
}
.Toastify__progress-bar-theme--dark {
  background: var(--toastify-color-progress-dark);
}
.Toastify__progress-bar--info {
  background: var(--toastify-color-progress-info);
}
.Toastify__progress-bar--success {
  background: var(--toastify-color-progress-success);
}
.Toastify__progress-bar--warning {
  background: var(--toastify-color-progress-warning);
}
.Toastify__progress-bar--error {
  background: var(--toastify-color-progress-error);
}
.Toastify__progress-bar-theme--colored.Toastify__progress-bar--info, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--success, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--warning, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--error {
  background: var(--toastify-color-transparent);
}

.Toastify__close-button {
  color: #fff;
  background: transparent;
  outline: none;
  border: none;
  padding: 0;
  cursor: pointer;
  opacity: 0.7;
  transition: 0.3s ease;
  -ms-flex-item-align: start;
      align-self: flex-start;
}
.Toastify__close-button--light {
  color: #000;
  opacity: 0.3;
}
.Toastify__close-button > svg {
  fill: currentColor;
  height: 16px;
  width: 14px;
}
.Toastify__close-button:hover, .Toastify__close-button:focus {
  opacity: 1;
}

@keyframes Toastify__trackProgress {
  0% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
.Toastify__progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 5px;
  z-index: var(--toastify-z-index);
  opacity: 0.7;
  transform-origin: left;
}
.Toastify__progress-bar--animated {
  animation: Toastify__trackProgress linear 1 forwards;
}
.Toastify__progress-bar--controlled {
  transition: transform 0.2s;
}
.Toastify__progress-bar--rtl {
  right: 0;
  left: initial;
  transform-origin: right;
}

.Toastify__spinner {
  width: 20px;
  height: 20px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: var(--toastify-spinner-color-empty-area);
  border-right-color: var(--toastify-spinner-color);
  animation: Toastify__spin 0.65s linear infinite;
}

@keyframes Toastify__bounceInRight {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  from {
    opacity: 0;
    transform: translate3d(3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(-25px, 0, 0);
  }
  75% {
    transform: translate3d(10px, 0, 0);
  }
  90% {
    transform: translate3d(-5px, 0, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
}
@keyframes Toastify__bounceInLeft {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(25px, 0, 0);
  }
  75% {
    transform: translate3d(-10px, 0, 0);
  }
  90% {
    transform: translate3d(5px, 0, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutLeft {
  20% {
    opacity: 1;
    transform: translate3d(20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(-2000px, 0, 0);
  }
}
@keyframes Toastify__bounceInUp {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  from {
    opacity: 0;
    transform: translate3d(0, 3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  75% {
    transform: translate3d(0, 10px, 0);
  }
  90% {
    transform: translate3d(0, -5px, 0);
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__bounceOutUp {
  20% {
    transform: translate3d(0, -10px, 0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0, 20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, -2000px, 0);
  }
}
@keyframes Toastify__bounceInDown {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0, -3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, 25px, 0);
  }
  75% {
    transform: translate3d(0, -10px, 0);
  }
  90% {
    transform: translate3d(0, 5px, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutDown {
  20% {
    transform: translate3d(0, 10px, 0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, 2000px, 0);
  }
}
.Toastify__bounce-enter--top-left, .Toastify__bounce-enter--bottom-left {
  animation-name: Toastify__bounceInLeft;
}
.Toastify__bounce-enter--top-right, .Toastify__bounce-enter--bottom-right {
  animation-name: Toastify__bounceInRight;
}
.Toastify__bounce-enter--top-center {
  animation-name: Toastify__bounceInDown;
}
.Toastify__bounce-enter--bottom-center {
  animation-name: Toastify__bounceInUp;
}

.Toastify__bounce-exit--top-left, .Toastify__bounce-exit--bottom-left {
  animation-name: Toastify__bounceOutLeft;
}
.Toastify__bounce-exit--top-right, .Toastify__bounce-exit--bottom-right {
  animation-name: Toastify__bounceOutRight;
}
.Toastify__bounce-exit--top-center {
  animation-name: Toastify__bounceOutUp;
}
.Toastify__bounce-exit--bottom-center {
  animation-name: Toastify__bounceOutDown;
}

@keyframes Toastify__zoomIn {
  from {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
@keyframes Toastify__zoomOut {
  from {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  to {
    opacity: 0;
  }
}
.Toastify__zoom-enter {
  animation-name: Toastify__zoomIn;
}

.Toastify__zoom-exit {
  animation-name: Toastify__zoomOut;
}

@keyframes Toastify__flipIn {
  from {
    transform: perspective(400px) rotate3d(1, 0, 0, 90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotate3d(1, 0, 0, 10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotate3d(1, 0, 0, -5deg);
  }
  to {
    transform: perspective(400px);
  }
}
@keyframes Toastify__flipOut {
  from {
    transform: perspective(400px);
  }
  30% {
    transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
    opacity: 1;
  }
  to {
    transform: perspective(400px) rotate3d(1, 0, 0, 90deg);
    opacity: 0;
  }
}
.Toastify__flip-enter {
  animation-name: Toastify__flipIn;
}

.Toastify__flip-exit {
  animation-name: Toastify__flipOut;
}

@keyframes Toastify__slideInRight {
  from {
    transform: translate3d(110%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInLeft {
  from {
    transform: translate3d(-110%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInUp {
  from {
    transform: translate3d(0, 110%, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInDown {
  from {
    transform: translate3d(0, -110%, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideOutRight {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(110%, 0, 0);
  }
}
@keyframes Toastify__slideOutLeft {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(-110%, 0, 0);
  }
}
@keyframes Toastify__slideOutDown {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, 500px, 0);
  }
}
@keyframes Toastify__slideOutUp {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, -500px, 0);
  }
}
.Toastify__slide-enter--top-left, .Toastify__slide-enter--bottom-left {
  animation-name: Toastify__slideInLeft;
}
.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right {
  animation-name: Toastify__slideInRight;
}
.Toastify__slide-enter--top-center {
  animation-name: Toastify__slideInDown;
}
.Toastify__slide-enter--bottom-center {
  animation-name: Toastify__slideInUp;
}

.Toastify__slide-exit--top-left, .Toastify__slide-exit--bottom-left {
  animation-name: Toastify__slideOutLeft;
}
.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right {
  animation-name: Toastify__slideOutRight;
}
.Toastify__slide-exit--top-center {
  animation-name: Toastify__slideOutUp;
}
.Toastify__slide-exit--bottom-center {
  animation-name: Toastify__slideOutDown;
}

@keyframes Toastify__spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}</style><style>:root {
  --ck-color-base-code-block: hsl(0, 0%, 20.8%);
}

div.comment_container[dark-mode="true"] {
  --ck-color-base-code-block: #f5deb3;
}

/* Code block css */
.comment_container pre {
  padding: 16px;
  color: var(--ck-color-base-code-block) !important;
  background: var(--gfg-background-200);
  border-radius: 10px;
  text-align: left;
  direction: ltr;
  tab-size: 4;
  white-space: pre-wrap;
  font-style: normal;
  min-width: 200px;
}

.comment_container code {
  background: var(--gfg-background-200);
  padding: 0.15em;
  border-radius: 2px;
}

.comment_container pre code {
  background: unset;
  padding: 0;
  border-radius: 0;
}

.comment_container code {
  font-size: 87.5%;
  color: #e83e8c;
  word-wrap: break-word;
}

.comment_container pre code {
  font-size: 14px;
  color: inherit;
  word-break: normal;
}

.comment_container code,
kbd,
pre,
samp {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
    "Courier New", monospace;
  font-size: 1em;
}

.modal-custom-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.modal-custom-header h6 {
  font-size: 18px;
  font-weight: 600;
  margin: 0;
}

.modal-comment-system-custom-template {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 20px;
  box-shadow: rgba(100, 100, 111, 0.3) 0px 7px 29px;
  background-color: #fff;
  border: none;
  border-radius: 12px;
  position: absolute;
  padding: 12px;
  width: fit-content;
  height: fit-content;
  max-height: 500px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  overflow: auto;
}

.modal-buttons-wrapper{
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
  gap: 8px;
}

.modal-buttons-wrapper > button:disabled{
  pointer-events: none;
  opacity: 0.8;
}

.modal-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  padding: 6px 12px;
  font-size: 12px;
  border: none;
  box-shadow: none;
  cursor: pointer;
  min-width: 80px;
}

.modal-action-success-buttons {
  background-color: #357960;
  color: #ffffff;
}

.modal-action-close-buttons {
  background-color: #f5f5f7;
  color: #9597a1;
}

.modal-custom-backdrop {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100dvh;
  background-color: rgba(0, 0, 0, 0.75);
  bottom: 0;
  left: 0;
  position: fixed;
  z-index: 100;
  overflow: hidden;
}

.custom-template-input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
  gap: 4px;
}

.custom-template-input-wrapper label {
  font-size: 14px;
  font-weight: 600;
}

.custom-template-input-wrapper input {
  border: none;
  background: #f2f2f2;
  padding: 6px;
  border-radius: 3px;
  width: 250px;
  outline: none;
  font-size: 14px;
  border-radius: 8px;
}
</style><style>:root {
  --gfg-comment-font-primary: var(--gfg-font-primary), var(--font-secondary);
  --gfg-comment-font-secondary: var(--gfg-font-secondary), var(--font-primary);
  --transition-time: 0.4s;
  /* color shades */
  --gfg-background-color: #ffffff;
  --gfg-color-header: blue;
  --color-gfg: #308d46;
  --color-black: #273239;
  --color-blue: #2c3e50;
  --gfg-body-color: white;
  --color-grey: #96a2a9;
  --gfg-tint-color: white;
  --gfg-selected-color: #ececec;
  --gfg-title-color: #121212;
  --gfg-subtitle-color: #121212;
  --gfg-tags-color: #989898;
  --gfg-text-color: #989898;
  --gfg-color-lg: #6d6d6d;
  --gfg-grey-bg: #f9f9f9;
  --gfg-darkgrey: #ebebeb;
  --gfg-light-bg: #d7efee;
  --gfg-tags-base-color: #308d46;
  --color-gfg-bg: rgba(48, 141, 70, 0.1);
  --gfg-wrapper-bg: #fafafa;
  --gfg-footer-text-color: #696969;
  --color-gfg-alternate: #308d46;
  --gfg-green-white: #308d46;
  --search-bg-color: #d2d2d2;
  --gfg-lightbg-color: rgba(235, 235, 235, 0.67);
  --gfg-body-color-alternate: #f0f0f0;
  --gfg-head-shadow: #1111112b;
  --scroller-color: #b6b6b6;
  --faded-green: #e8f6eeb3;
  --navy-blue-to-white: #0f2b3c;
  --black-to-white: #000000;
  --lightblue-to-lightblack: #eff8f3;
  --white-to-lightgrey: white;
  --white-to-lightblack: white;
  --primary-10: #aed2b8;
  --gfg-primary: #2f8d46;
  --gfg-secondary: #0f2b3c;
  --report-background: "#ffffff";
  --pagination-page-number-color: #707070;
  --description-text-color: #3b3b3b;
  --pagination-active-bg-color: #107028;
  --subheader-bg-color: #fff;
  --scrollbar-track-color: #ebebeb;
  --breadcumb-active-color: #0f2b3c;
  --google-search-input-bg: #e6e6e6;
  --gfg-footer-background: #fff;
  --gfg-footer-border: #dedede;
  --video-card-shadow: #00000029;
  --theme-selector-bg: #efefef;
  --gfg-color: #308d46;
  --vote-button: #e5e5e5;
  --gfg-text-secondary-color: #6c757d;
  --gfg-text-secondary-color-hover: #6c757d;
  --hashtag-color: #357960;
  --deleted-comment: #f4f4f8;
  --gfg-dropdown-menu: #ffffff;
  --gfg-dropdown-item: #212529;
  --gfg-dropdown-hover: #e9ecef;
  --gfg-text-grey: #6c757d;
  --gfg-text-danger: #dc3545;
  --gfg-text-success: #28a745;
  --gfg-btn-light-border: #f8f9fa;
  --gfg-btn-light-background: #f8f9fa;
  --gfg-btn-light-border-hover: #dae0e5;
  --gfg-btn-light-background-hover: #e2e6ea;
  --gfg-btn-shadow: 0 0 0 0.2rem rgb(0 123 255 / 25%);

  /* New Codes */
  --gfg-background-100: #fff;
  --gfg-background-200: #f5f5f7;
  --gfg-background-300: #f5f5f7;
  --gfg-background-dark-100: #6e6e73;

  --gfg-text-100: #0e0e12;
  --gfg-text-200: #1d1d1f;

  --gfg-border-100: rgba(14, 14, 18, 0.05);

  --gfg-meta-100: #6e6e73;
}

div.comment_container[dark-mode="true"] {
  --gfg-upper-half-bg: transparent
    linear-gradient(180deg, #484848 0%, #111111 100%) 0% 0% no-repeat
    padding-box;
  --gfg-background-color: #111111;
  --gfg-color-header: red;
  --color-black: #ffffff;
  --color-blue: #ffffff;
  --color-grey: #ffffff;
  --gfg-body-color: #171b1d;
  --gfg-wrapper-bg: #292929;
  --gfg-tint-color: #222221;
  --gfg-selected-color: #39393c;
  --gfg-title-color: #ffffff;
  --gfg-subtitle-color: #ffffff;
  --gfg-tags-color: #989898;
  --gfg-text-color: #989898;
  --gfg-color-lg: #ffffff;
  --gfg-grey-bg: #2a2a2c;
  --gfg-darkgrey: #404040;
  --gfg-light-bg: #222221;
  --gfg-tags-base-color: #308d46;
  --search-bg-color: #2a2a2c;
  --search-border-color: transparent;
  --color-gfg-alternate: #2a2a2c;
  --gfg-footer-text-color: #ffffff;
  --gfg-article-text-color: #ffffff;
  --search-text-color: #ffffff;
  --gfg-sidebars-color: #2a2a2c;
  --gfg-lightbg-color: #222221;
  --gfg-rightbar-header: #ffffff;
  --gfg-tech-scripter: #ffffff;
  --gfg-hover-color: #2a2a2a;
  --gfg-body-color-alternate: #131417;
  --gfg-head-shadow: #8471712b;
  --gfg-green-white: #ffffff;
  --faded-green: #ffffff24;
  --navy-blue-to-white: #ffffffb3;
  --black-to-white: #ffffff;
  --lightblue-to-lightblack: #292929;
  --white-to-lightgrey: #8080801a;
  --white-to-lightblack: #292929;
  --report-background: "#111111";
  --pagination-page-number-color: #707070;
  --description-text-color: #a5a5a5;
  --pagination-active-bg-color: #2f8d46;
  --subheader-bg-color: #222221;
  --scrollbar-track-color: rgba(54, 48, 48, 0.8);
  --breadcumb-active-color: #2f8d46;
  --google-search-input-bg: #575757;
  --gfg-footer-background: #111111;
  --gfg-footer-border: #3d3d3d;
  --video-card-shadow: #e0e0e014;
  --theme-selector-bg: #5e5e5e;
  --vote-button: #4a494b;
  --gfg-text-secondary-color: #ffffff;
  --gfg-text-secondary-color-hover: #c1c6ca;
  --deleted-comment: hsl(270, 1%, 29%);
  --dark-brightness: brightness(0);
  --dark-invert: invert(1);
  --gfg-dropdown-menu: hsl(270, 1%, 29%);
  --gfg-dropdown-item: #ffffff;
  --gfg-dropdown-hover: #000000;
  --gfg-text-grey: #9b9696;
  --gfg-text-danger: #ffffff;
  --gfg-text-success: #ffffff;
  --gfg-btn-light-border: unset;
  --gfg-btn-light-background: transparent;
  --gfg-btn-light-border-hover: unset;
  --gfg-btn-light-background-hover: transparent;
  --gfg-btn-shadow: none;

  /* New Codes */
  --gfg-background-100: #0a0e0f;
  --gfg-background-200: #202426;
  --gfg-background-300: #252b2e;
  --gfg-background-dark-100: #252b2e;

  --gfg-text-100: #e9e9ea;
  --gfg-text-200: #e9e9ea;

  --gfg-border-100: #5e5e5e;

  --gfg-meta-100: #e9e9ea;
}

/* NEW CSS STARTS HERE */

body,
html {
  margin: 0px;
  padding: 0px;
}
body::-webkit-scrollbar,
html::-webkit-scrollbar {
  width: 6px;
}
body::-webkit-scrollbar-track,
html::-webkit-scrollbar-track {
  background-color: #f1f1f1;
  /* Set the background color of the scrollbar track */
}
body::-webkit-scrollbar-thumb,
html::-webkit-scrollbar-thumb {
  background-color: #6e6e73;
  /* Set the color of the scrollbar thumb */
  border-radius: 4px;
  /* Round the corners of the thumb */
}
body::-webkit-scrollbar-thumb:hover,
html::-webkit-scrollbar-thumb:hover {
  background-color: #555;
  /* Set the color of the thumb on hover */
}

/* Shimmer CSS Starts */
.gfg-comment-shimmer-container {
  overflow: hidden;
  border-radius: 4px;
  background-color: var(--gfg-background-200);
}
.gfg-comment-shimmer-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  animation: loading 1.5s infinite;
  overflow: hidden;
  border-radius: 4px;
  width: 100%;
}
.gfg-comment-shimmer {
  width: 25%;
  height: 100%;
  background: var(--gfg-background-300);
  box-shadow: 20px 10px 30px 30px var(--gfg-background-300);
}

@keyframes loading {
  0% {
    transform: translateX(-100%);
  }
  50% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(100%);
  }
}

/* Shimmer CSS Ends */

/* Circular Loader */
.circular_loader {
  height: 20px;
  width: 20px;
  position: relative;
  margin: 0 auto;
}
.circular_loader > span {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  height: 20px;
  width: 20px;
  -webkit-animation: circular_animation_2 2s cubic-bezier(0.77, 0, 0.175, 1)
    infinite;
  animation: circular_animation_2 2s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}
.circular_loader > span::before,
.circular_loader > span::after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  height: 12px;
  width: 12px;
  background: #fff;
  border-radius: 50%;
  -webkit-animation: circular_animation_3 2s cubic-bezier(0.77, 0, 0.175, 1)
    infinite;
  animation: circular_animation_3 2s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}
.circular_loader > span::after {
  -webkit-animation: circular_animation_4 2s cubic-bezier(0.77, 0, 0.175, 1)
    infinite;
  animation: circular_animation_4 2s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}
.circular_loader::after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  width: 12px;
  height: 12px;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  background: #fff;
  border-radius: 50%;
  -webkit-animation: circular_animation_1 2s cubic-bezier(0.77, 0, 0.175, 1)
    infinite;
  animation: circular_animation_1 2s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}

@-webkit-keyframes circular_animation_1 {
  0% {
    -webkit-transform: scale(0);
    opacity: 0;
  }
  50% {
    -webkit-transform: scale(1);
    opacity: 1;
  }
  100% {
    -webkit-transform: scale(0);
    opacity: 0;
  }
}
@keyframes circular_animation_1 {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  50% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(0);
    opacity: 0;
  }
}
@-webkit-keyframes circular_animation_2 {
  0% {
    -webkit-transform: rotate(0deg);
  }
  50% {
    -webkit-transform: rotate(180deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
@keyframes circular_animation_2 {
  0% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(180deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes circular_animation_3 {
  0% {
    -webkit-transform: translate3d(0, 0, 0) scale(1);
  }
  50% {
    -webkit-transform: translate3d(-16px, 0, 0) scale(0.5);
  }
  100% {
    -webkit-transform: translate3d(0, 0, 0) scale(1);
  }
}
@keyframes circular_animation_3 {
  0% {
    transform: translate3d(0, 0, 0) scale(1);
  }
  50% {
    transform: translate3d(-16px, 0, 0) scale(0.5);
  }
  100% {
    transform: translate3d(0, 0, 0) scale(1);
  }
}
@-webkit-keyframes circular_animation_4 {
  0% {
    -webkit-transform: translate3d(0, 0, 0) scale(1);
  }
  50% {
    -webkit-transform: translate3d(16px, 0, 0) scale(0.5);
  }
  100% {
    -webkit-transform: translate3d(0, 0, 0) scale(1);
  }
}
@keyframes circular_animation_4 {
  0% {
    transform: translate3d(0, 0, 0) scale(1);
  }
  50% {
    transform: translate3d(16px, 0, 0) scale(0.5);
  }
  100% {
    transform: translate3d(0, 0, 0) scale(1);
  }
}

.comment_container {
  padding: 20px;
  padding-bottom: 70px;
  color: var(--color-black) !important;
  background-color: var(--gfg-background-100) !important;
  font-family: var(--gfg-comment-font-primary);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow: visible;
  -webkit-overflow-scrolling: touch;
}

.comment_container .load_view__all__comments {
  text-align: center;
  padding: 20px;
  background-color: var(--gfg-background-300);
  border-radius: 10px;
  color: var(--gfg-text-100);
  font-size: 16px;
}

.comment_container .load_view__all__comments a {
  font-weight: bold !important;
  color: var(--color-gfg);
}

.comment_container > code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
    monospace;
}
.comment_container .tooltip_text {
  visibility: hidden;
  font-family: var(--gfg-comment-font-secondary);
  position: absolute;
  z-index: 10;
  width: 120px;
  color: #f5f5f7;
  font-size: 12.5px;
  background-color: var(--gfg-background-dark-100);
  border-radius: 10px;
  padding: 10px 15px 10px 15px;
}
.comment_container .tooltip_text {
  top: -45px;
  left: -100%;
}
.comment_container .tooltip_text::before {
  content: "";
  position: absolute;
  transform: rotate(45deg);
  background-color: var(--gfg-background-dark-100);
  padding: 5px;
  z-index: 1;
}
.comment_container .hover_text:hover .tooltip_text {
  visibility: visible;
}
.comment_container .tooltip_text::before {
  top: 80%;
  left: 45%;
}
.comment_container .hover_text {
  position: relative;
  display: inline-block;
  font-family: Arial;
  text-align: center;
}
.comment_container .loader_parent {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  grid-gap: 5px;
  align-items: center;
  justify-content: center;
}
.comment_container .gfg-loader {
  position: relative;
  content: "";
  box-sizing: border-box;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid #ccc;
  border-top-color: grey;
  animation: spinner 0.6s linear infinite;
}
.comment_container .errorMessage {
  position: fixed !important;
  left: 10px !important;
  bottom: 10px !important;
  z-index: 10;
}
.comment_container .user_image {
  width: 35px;
  height: 35px;
  border-radius: 50%;
}
.comment_container .image_shimmer .gfg-comment-shimmer-container {
  border-radius: 50%;
  overflow: hidden;
}
.comment_container .comment_shimmer {
  display: grid;
  grid-template-columns: max-content 1fr;
  grid-gap: 12px;
  margin-top: 25px;
}
.comment_container .comment_shimmer .right {
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 8px;
}
.comment_container .comment_shimmer .right .inner {
  display: grid;
  grid-template-columns: repeat(3, max-content);
  align-items: center;
  justify-content: flex-start;
  grid-gap: 8px;
  margin-top: 15px;
}
.comment_container .custom_dropdown__menu {
  background-color: var(--gfg-background-300) !important;
  border-radius: 8px;
  padding: 12px;
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 14px;
  min-width: 120px;
  position: absolute;
  top: 36px;
  right: 4px;
  z-index: 2;
  box-shadow: 0px 0px 12px 1px rgba(0, 0, 0, 0.12);
}
.comment_container .custom_dropdown__menu .dropdown-item {
  background-color: transparent;
  outline: none;
  border: none;
  margin: 0px;
  padding: 0px;
  text-align: left;
  cursor: pointer;
  font-size: 12.5px;
  color: var(--gfg-text-200);
  font-family: var(--gfg-comment-font-primary);
  transition: all 0.15s linear;
  text-decoration: none;
}
.comment_container .custom_dropdown__menu .dropdown-item:hover {
  color: var(--gfg-text-100);
}
.comment_container .editor_container {
  display: grid;
  grid-template-columns: max-content 1fr;
  align-items: flex-start;
  justify-content: center;
  grid-gap: 16px;
}
.comment_container .editor_container .editor_content .tox-tinymce {
  border: none;
  background-color: var(--gfg-background-200);
  border-radius: 12px;
}
.comment_container .editor_container .editor_content .tox-tinymce .tox-toolbar {
  background: transparent;
}
.comment_container
  .editor_container
  .editor_content
  .tox-tinymce
  .tox-toolbar-overlord {
  background: transparent;
}
.comment_container
  .editor_container
  .editor_content
  .tox-tinymce
  .tox-toolbar__group:not(:last-of-type) {
  border: none;
  padding: 0px;
  background: transparent;
}
.comment_container
  .editor_container
  .editor_content
  .tox-tinymce
  .tox-editor-header {
  border-bottom: solid 1px var(--gfg-border-100);
  background: transparent;
}
.comment_container
  .editor_container
  .editor_content
  .tox-tinymce
  .tox-edit-area__iframe {
  background-color: transparent;
}
.comment_container
  .editor_container
  .editor_content
  .tox-tinymce
  .tox-toolbar__primary {
  background: transparent;
  padding: 0px 10px;
}
.comment_container .editor_container .editor_content .action_buttons {
  display: grid;
  grid-template-columns: 1fr repeat(4, max-content);
  align-items: center;
  justify-content: flex-end;
  margin-top: 10px;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .anonymous_checkbox {
  margin-right: 10px;
  accent-color: #357960;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .anonymous_comment_label {
  font-size: 12px;
  font-family: arial, sans-serif;
  margin-right: 10px;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  > button:disabled {
  pointer-events: none;
  opacity: 0.8;
}
.comment_container .editor_container .editor_content .action_buttons .btn {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  padding: 6px 12px;
  grid-gap: 5px;
  font-size: 12px;
  border: none;
  box-shadow: none;
  cursor: pointer;
  min-width: 80px;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .btn
  .icon {
  width: 18px;
  height: 18px;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .btn
  .icon
  > svg {
  width: 100%;
  height: 100%;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .btn.green {
  background-color: #357960;
  color: white;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .btn.green
  .icon
  > svg
  > path {
  stroke: white;
}
.comment_container .editor_container .editor_content .action_buttons .btn.grey {
  background-color: var(--gfg-background-200);
  color: #9597a1;
  width: max-content;
  justify-self: end;
  margin-right: 10px;
}
.comment_container
  .editor_container
  .editor_content
  .action_buttons
  .btn.loader {
  display: block;
}
.comment_container .top_container .meta_information {
  background: 0% 0% no-repeat padding-box padding-box #dfe7fa;
  font-family: var(--gfg-comment-font-secondary);
  font-size: 14px;
  color: #333;
  font-weight: 600;
  padding: 12px;
  border-radius: 10px;
  margin-bottom: 35px;
}
.comment_container .top_container .meta_information > span {
  display: grid;
  align-items: center;
  justify-content: center;
}
.comment_container .top_container .top_container__contents {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  align-items: center;
  justify-content: space-between;
  margin-bottom: 35px;
}
.comment_container .top_container .top_container__contents .left {
  display: grid;
  grid-template-columns: repeat(3, max-content);
  align-items: center;
  justify-content: center;
  gap: 10px;
}
.comment_container .top_container .top_container__contents .left .title {
  font-family: var(--gfg-comment-font-secondary);
  color: var(--gfg-text-100);
  font-size: 18px;
  font-weight: 700;
}
.comment_container .top_container .top_container__contents .left .threads {
  color: var(--gfg-text-100);
  font-size: 14px;
  font-family: var(--gfg-comment-font-secondary);
}
.comment_container
  .top_container
  .top_container__contents
  .left
  .redirection
  > svg
  > path {
  stroke: var(--gfg-text-200);
}
.comment_container .top_container .top_container__contents .right {
  position: relative;
}
.comment_container
  .top_container
  .top_container__contents
  .right
  .filters_dropdown {
  background-color: var(--gfg-background-200) !important;
  border-radius: 10px;
  padding: 0px 15px;
  font-family: var(--gfg-comment-font-secondary);
  font-size: 14px;
  border: none;
  outline: none;
  color: var(--gfg-text-100) !important;
  cursor: pointer;
  display: grid;
  grid-template-columns: repeat(2, max-content);
  min-width: 120px;
  align-items: center;
  justify-content: space-between;
  height: 34px;
  grid-gap: 6px;
}
.comment_container
  .top_container
  .top_container__contents
  .right
  .filters_dropdown
  .rotate {
  transform: rotate(180deg);
  transform-origin: center;
  transition: all 0.2s linear;
}
.comment_container
  .top_container
  .top_container__contents
  .right
  .filters_dropdown
  .normal {
  transform: rotate(0deg);
  transform-origin: center;
  transition: all 0.2s linear;
}
.comment_container
  .top_container
  .top_container__contents
  .right
  .filters_dropdown
  .dropdown_icon
  > svg
  > path {
  stroke: var(--gfg-text-200);
}
.comment_container .bottom_container .bottom_contents {
  margin-top: 20px;
}
.comment_container .bottom_container .bottom_contents .no_comments {
  margin: 0px;
  text-align: center;
  font-family: var(--gfg-comment-font-secondary);
  color: var(--gfg-text-100);
  font-size: 16px;
}
.comment_container .bottom_container .bottom_contents .single_comment {
  padding: 1rem;

  &.focused {
    animation: focused_comment 2s linear;
  }
}

@keyframes focused_comment {
  0% {
    background-color: rgba(255, 255, 0, 0.1);
  }

  20% {
    background-color: rgba(255, 255, 0, 0.2);
  }

  60% {
    background-color: rgba(255, 255, 0, 0.2);
  }

  100% {
    background-color: transparent;
  }
}

.comment_container .bottom_container .bottom_contents .single_comment .items {
  display: grid;
  grid-template-columns: max-content 1fr;
  grid-gap: 16px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right {
  width: 100%;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  justify-content: space-between;
  padding-top: 4px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  justify-content: center;
  width: max-content;
  grid-gap: 10px;
  height: max-content;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .pinned_image {
  width: 22px;
  height: 22px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .pinned_image
  > svg {
  width: 100%;
  height: 100%;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .user_name {
  font-family: var(--gfg-comment-font-secondary);
  color: var(--gfg-text-100);
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  width: max-content;
  gap: 6px;
  text-decoration: none;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .user_time {
  color: var(--gfg-meta-100);
  font-family: var(--gfg-comment-font-secondary);
  font-size: 14px;
  position: relative;
}

.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .user_time:hover
  .user_time_details {
  opacity: 1;
}

.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .user_time
  .user_time_details {
  position: absolute;
  bottom: 160%;
  left: 0%;
  width: max-content;
  background-color: white;
  color: #888;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 2px 6px;
  border-radius: 4px;
  opacity: 0;
  transition: all 0.3s ease-in-out;
  font-size: 12px;
}

.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .user_info
  .user_banned {
  color: white;
  font-family: var(--gfg-comment-font-secondary);
  font-size: 1rem;
  padding: 5px 10px;
  background-color: var(--gfg-text-danger);
}

.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .dropdown
  .dropdown_content {
  position: relative;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .dropdown
  .dropdown_content
  .dropdown_toggle__btn {
  margin: 0px;
  padding: 0px;
  background-color: transparent;
  border: none;
  box-shadow: none;
  cursor: pointer;
  margin-right: 4px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .meta
  .dropdown
  .dropdown_content
  .dropdown_toggle__btn
  > span
  > svg {
  width: 100%;
  height: 14px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .restricted_comments {
  margin-top: 20px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .restricted_comments
  .restricted_comments__content {
  color: #a5a5a5;
  background-color: var(--gfg-background-200);
  border-radius: 10px;
  font-size: 14px;
  font-family: var(--gfg-comment-font-secondary);
  display: grid;
  grid-template-columns: max-content 1fr;
  grid-gap: 10px;
  align-items: center;
  justify-content: flex-start;
  padding: 10px 12px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .restricted_comments
  .restricted_comments__content
  .image {
  width: 20px;
  height: 20px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .restricted_comments
  .restricted_comments__content
  .image
  svg {
  width: 100%;
  height: 100%;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .restricted_comments
  .restricted_comments__content
  .user_name {
  color: #666b71;
  font-weight: 600;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .deleted_comments__reply {
  color: #9597a1;
  font-family: var(--gfg-comment-font-secondary);
  font-size: 14px;
  font-style: normal;
  font-weight: 600;
  margin-top: 10px;
  display: block;
  width: max-content;
  cursor: pointer;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text {
  max-width: calc(100vw - 120px);
  margin-top: 10px;
  overflow-x: auto;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  img {
  max-width: 100%;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text::-webkit-scrollbar {
  height: 4px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text::-webkit-scrollbar-track {
  background-color: #f1f1f1;
  /* Set the background color of the scrollbar track */
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text::-webkit-scrollbar-thumb {
  background-color: #6e6e73;
  /* Set the color of the scrollbar thumb */
  border-radius: 4px;
  /* Round the corners of the thumb */
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text::-webkit-scrollbar-thumb:hover {
  background-color: #555;
  /* Set the color of the thumb on hover */
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  .mention {
  color: #2f8d46;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  > * {
  -webkit-transform: translateZ(0px);
  -webkit-transform: translate3d(0, 0, 0);
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  > * {
  font-family: var(--gfg-comment-font-primary) !important;
  color: var(--gfg-text-100) !important;
  font-size: 15px !important;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  .height_bandwidth {
  max-height: 200px;
  overflow: hidden;
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  .hashtag {
  color: var(--hashtag-color);
  text-decoration: none;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  .hashtags {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  justify-content: flex-start;
  grid-gap: 10px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .text
  .hashtags
  .item {
  background-color: #f1f8f5;
  color: var(--hashtag-color);
  font-size: 14px;
  border-radius: 14px;
  width: max-content;
  text-decoration: none;
  padding: 2px 10px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .read_container {
  text-align: right;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .read_container
  .read_btn {
  background-color: transparent;
  border: none;
  box-shadow: none;
  color: var(--gfg-text-200);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom {
  margin-top: 15px;
  display: grid;
  grid-auto-columns: max-content;
  grid-auto-flow: column;
  grid-gap: 28px;
  align-items: center;
  justify-content: flex-start;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  align-items: center;
  justify-content: flex-start;
  grid-gap: 15px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes,
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  align-items: center;
  justify-content: flex-start;
  grid-gap: 8px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > span,
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > span {
  color: var(--gfg-text-200);
  font-weight: 400;
  font-size: 14px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button,
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button {
  box-shadow: none;
  border: none;
  background-color: transparent;
  padding: 0px;
  margin: 0px;
  width: 17px;
  height: 17px;
  cursor: pointer;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button:disabled,
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button:disabled {
  pointer-events: none;
  opacity: 0.25;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button
  > svg,
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button
  > svg {
  width: 100%;
  height: 100%;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button
  > svg
  > path {
  stroke: var(--gfg-text-200);
  fill: none;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button:hover
  > svg
  > path {
  transition: all 0.1s linear;
  stroke: #2f8d46;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .up_votes
  > button.voted
  > svg
  > path {
  fill: #2f8d46;
  stroke: #2f8d46;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button
  > svg
  > path {
  stroke: var(--gfg-text-200);
  fill: none;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button:hover
  > svg
  > path {
  transition: all 0.1s linear;
  stroke: #e02828;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .voting_container
  .down_votes
  > button.voted
  > svg
  > path {
  fill: #e02828;
  stroke: #e02828;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .replies_container {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  align-items: center;
  justify-content: flex-start;
  grid-gap: 8px;
  color: var(--gfg-meta-100);
  font-size: 14px;
  font-weight: 600;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .replies_container
  .reply_container {
  cursor: pointer;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .bottom
  .replies_container
  .show_reply__container {
  color: #9597a1;
  cursor: pointer;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .reply_editor_container {
  margin-top: 25px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment
  .items
  .right
  .replied_comments {
  margin-top: 30px;
}
.comment_container
  .bottom_container
  .bottom_contents
  .single_comment:nth-child(n + 2) {
  margin-top: 25px;
}
.comment_container .bottom_container .load_more__comments {
  display: grid;
  width: 100%;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
}
.comment_container .bottom_container .load_more__comments .btn {
  background: transparent;
  color: #9597a1;
  font-weight: 600;
  box-shadow: none;
  border: none;
  font-size: 12.5px;
  cursor: pointer;
}

@media screen and (max-width: 500px) {
  .comment_container {
    padding: 10px;
  }
  .comment_container .user_image {
    width: 30px;
    height: 30px;
  }
  .comment_container .filters_dropdown {
    font-size: 12px !important;
    height: 30px !important;
    min-width: 90px !important;
  }
  .comment_container .top_container__contents {
    margin-bottom: 25px !important;
  }
  .comment_container .editor_container {
    grid-gap: 10px;
  }
  .comment_container .bottom_contents {
    margin-top: 15px !important;
  }
  .comment_container .single_comment:nth-child(n + 2) {
    margin-top: 15px !important;
  }
  .comment_container .single_comment .items {
    grid-gap: 10px !important;
  }
  .comment_container .show_reply__container {
    font-size: 12px;
  }
  .comment_container .dropdown_toggle__btn > span > svg {
    height: 12px !important;
  }
  .comment_container .user_info .user_name {
    font-size: 14px !important;
  }
  .comment_container .user_info .user_name > img {
    width: 16px !important;
    height: 16px !important;
  }
  .comment_container .user_info .user_time {
    font-size: 12px !important;
  }
  .comment_container .reply_container {
    font-size: 12px !important;
  }
  .comment_container .bottom {
    grid-gap: 15px !important;
  }
  .comment_container .bottom .voting_container {
    grid-gap: 15px !important;
  }
  .comment_container .bottom .voting_container > .up_votes > button,
  .comment_container .bottom .voting_container > .down_votes > button {
    width: 14px !important;
    height: 14px !important;
  }
  .comment_container .bottom .voting_container > .up_votes > span,
  .comment_container .bottom .voting_container > .down_votes > span {
    font-size: 12px !important;
  }
}

.commenting_as {
  font-size: 14px;
}
</style><link rel="stylesheet" type="text/css" id="mce-u0" href="./Allocate Minimum Pages _ op_files/skin.min.css"></head><body data-theme="light" style="overflow: unset;"><div id="__next" data-reactroot=""><div><div class="gfg_header_wrapper"><div class="root gfg_header__root" data-dark-mode="false" style="display:unset"><div id="comp"><div class="gfgheader_parentContainer"><div class="containerWrapper " id="topMainHeader"><div class="headerContainer"><a class="headerMainLogo" href="https://www.geeksforgeeks.org/"><div class="logo"><img class="gfgLogoImg normal" src="./Allocate Minimum Pages _ op_files/gfg-gg-logo.svg" alt="geeksforgeeks" width="60" height="30"></div></a><ul class="headerMainList"><li class="headerMainListItem"><span style="display:flex;align-items:center" class="genericHeaderListClass"><div style="display:inline">Courses<div>
                <div style="
                  background: undefined;
                  position: absolute;
                  border-radius: 4px;
                  font-size: 11px;
                  color: white;
                  padding: 2px 5px !important;
                  top: -12px;
                  left: 15%;
                ">
                  
                </div>
              </div></div><i class="gfg-icon   gfg-icon-black-down-carrot genericHeaderListClass" style="position:relative;left:2px;top:0px"></i></span></li><li class="headerMainListItem"><span style="display:flex;align-items:center" class="genericHeaderListClass"><div style="display:inline">Tutorials<div></div></div><i class="gfg-icon   gfg-icon-black-down-carrot genericHeaderListClass" style="position:relative;left:2px;top:0px"></i></span></li><li class="headerMainListItem"><span style="display:flex;align-items:center" class="genericHeaderListClass"><div style="display:inline">Practice<div></div></div><i class="gfg-icon   gfg-icon-black-down-carrot genericHeaderListClass" style="position:relative;left:2px;top:0px"></i></span></li><li class="headerMainListItem"><span style="display:flex;align-items:center" class="genericHeaderListClass"><div style="display:inline">Jobs<div></div></div><i class="gfg-icon   gfg-icon-black-down-carrot genericHeaderListClass" style="position:relative;left:2px;top:0px"></i></span></li></ul><div class="header-main__container" style="display:flex;flex-flow:row-reverse;width:100%;align-items:center"><div class="mainContainer"><div class="defaultProfileImg">H</div></div><div style="margin:0px 10px;display:flex;cursor:pointer"><div id="google_translate_element" style="display:none"></div><span><i class="gfg-icon   gfg-icon-black-translate "></i></span></div><div class="notification_container"><div class="notification-bell-icon"><svg width="24" height="24" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16.0714 7.71408C16.0714 6.29327 15.507 4.93066 14.5024 3.926C13.4977 2.92135 12.1351 2.35693 10.7143 2.35693C9.2935 2.35693 7.93089 2.92135 6.92623 3.926C5.92157 4.93066 5.35716 6.29327 5.35716 7.71408C5.35716 13.9641 2.67859 15.7498 2.67859 15.7498H18.75C18.75 15.7498 16.0714 13.9641 16.0714 7.71408Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12.259 19.3213C12.102 19.5919 11.8767 19.8165 11.6056 19.9727C11.3345 20.1288 11.0272 20.211 10.7143 20.211C10.4015 20.211 10.0941 20.1288 9.82305 19.9727C9.55196 19.8165 9.32665 19.5919 9.16968 19.3213" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg></div></div><div class="darkMode-wrap darkMode-wrap-desktop" data-mode="Switch to Dark Mode"><button data-gfg-action="toggleGFGTheme" aria-label="Toggle GFG Theme"><div class="darkMode-wrap-red-dot" style="display: block;"></div><i class="gfg-icon gfg-icon_dark-mode"></i></button><span class="darkModeTooltipText">Switch to Dark Mode</span></div><div class="gs-plus-suggestion-container" style="background:#308D465e;padding:2px;border-radius:7px"><div class="gs-input_wrapper gs-show-search-bar"><span class="flexR gs-search-icon"><i class="gfg-icon   gfg-icon-grey-search "></i></span><form class="gs-form"><input type="text" value="" placeholder="Search..." class="gs-input"></form><span class="flexR gs-toggle-icon"><i class="gfg-icon   gfg-icon-grey-cancel "></i></span></div><div style="display:none" class="suggestion_box"><div class="suggestion_box_collection" style="border-radius:0 0 9px 9px"><div class="suggestion_box_collection_item suggestion_box_collection_color_highlighted"><i class="gfg-icon   gfg-icon-grey-search "></i><span>Data Structure</span></div><div class="suggestion_box_collection_item suggestion_box_collection_color_highlighted"><i class="gfg-icon   gfg-icon-grey-search "></i><span>Java</span></div><div class="suggestion_box_collection_item suggestion_box_collection_color_highlighted"><i class="gfg-icon   gfg-icon-grey-search "></i><span>Python</span></div><div class="suggestion_box_collection_item suggestion_box_collection_color_highlighted"><i class="gfg-icon   gfg-icon-grey-search "></i><span>HTML</span></div><div class="suggestion_box_collection_item suggestion_box_collection_color_highlighted"><i class="gfg-icon   gfg-icon-grey-search "></i><span>Interview Preparation</span></div></div></div></div></div></div></div></div></div><div id="script"></div></div></div><div class="jsx-c095eb98ac24c0d7"><section class="sidebar_gfg_sidebar__XSwbO"><div class="sidebar_sidebar_contents__Dp56z for_problems"><div class="sidebar_closed_sidebar__195Vi sidebar_icon_menu__7aYZh"><i aria-hidden="true" class="large icon sidebar_icon__9X1zz sidebar"></i><div class="sidebar_phone_menu__yZQxO"><p>Menu</p><i aria-hidden="true" class="large icon sidebar_icon__9X1zz arrow up"></i></div></div><div class="sidebar_opened_sidebar__5QkjI" id="scrollableContainer"><div class="sidebar_opened_sidebar__inner__A9r6V"><div class="sidebar_header__08vDb sidebar_header"><button class="ui button sidebar_close_icon__m8T6F"><i aria-hidden="true" class="icon undefined close"></i><i aria-hidden="true" class="icon undefined arrow down"></i></button><p href="/explorefalse"><i aria-hidden="true" class="icon angle left"></i>Back to Explore Page</p></div></div></div><div class="sidebar_overlay__CxZeC"></div></div></section><div class="problems_problem_page__G7vws problem_page__container "><section class="doubtSupport_ds_container__AaauO"><span id="ds_activator" class="doubtSupport_ds_activator___1OvZ"><span class="doubtSupport_container__7Y9Zz"><img src="./Allocate Minimum Pages _ op_files/chatIcon-1653561581.svg" alt="" class="ui image"></span></span><div id="ds-content-container" class="doubtSupport_ds_contents__P_jrl doubtSupport_ds_contents__min__LDY_A false" style="display: none;"><div class="doubtSupport_ds_contents__toolbar_grid__WlUdN"><span class="doubtSupport_right__UYnn_"><span class="doubtSupport_icons__R289q doubtSupport_hide_content_mob__YdoNG"><span style="box-sizing: border-box; display: inline-block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative; max-width: 100%;"><span style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; max-width: 100%;"><img alt="" aria-hidden="true" src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2725%27%20height=%2725%27/%3e" style="display: block; max-width: 100%; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px;"></span><img alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" decoding="async" data-nimg="intrinsic" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%;"><noscript></noscript></span></span><span class="doubtSupport_icons__R289q"><span style="box-sizing: border-box; display: inline-block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative; max-width: 100%;"><span style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; max-width: 100%;"><img alt="" aria-hidden="true" src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2725%27%20height=%2725%27/%3e" style="display: block; max-width: 100%; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px;"></span><img alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" decoding="async" data-nimg="intrinsic" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%;"><noscript></noscript></span></span></span></div><div class="doubtSupport_tab_div__j4bFz"><div><div class="ui secondary menu"><a class="active item">Ask A Doubt</a><a id="my_doubts" class="disabled item">My Doubts</a></div><div class="ui segment active tab"><div class="premiumExplore_primium_explore_container__WbrO8"><img src="./Allocate Minimum Pages _ op_files/DoubtSupport_1726038182.png" class="ui image premiumExplore_suggestion_image__C5nB_ premiumExplore_doubt_support_image_size__kRVIA"><div class="premiumExplore_btn_para_container__3X_zm null"><p>Upgrade to Premium for Doubt Support across all your problems and courses.</p><a class="premiumExplore_premium_btn__3SKIN" target="_blank" rel="noopener noreferrer" href="https://www.geeksforgeeks.org/geeksforgeeks-premium-subscription"><span> Explore Premium</span><i aria-hidden="true" class="icon premiumExplore_icons__mnt9V"><img src="./Allocate Minimum Pages _ op_files/Group 37416_1726036710.png" alt="Redirection Icon" width="11px" height="11px" class="ui image"></i></a></div></div></div></div></div></div></section><div class="problems_problem_page_container__jtoHA"><div class="vertical reflex-container"><div class="pane-content vertical reflex-element" style="flex: 0.5 1 0%;"><div class="problems_left_section__OndDL "><div class="problems_header__E09Dq problems_button_sidebar__D4lXX"><div class="ui pointing secondary problems_header_menu__aKU8f menu"><a class="green active item problems_header_menu__items__BUrou"><i aria-hidden="true" class="code icon"></i>Problem</a><a class="green item problems_header_menu__items__BUrou"><i aria-hidden="true" class="file alternate outline icon"></i>Editorial</a><a class="green item problems_header_menu__items__BUrou"><i aria-hidden="true" class="clock outline icon"></i>Submissions</a><a class="green item problems_header_menu__items__BUrou"><i aria-hidden="true" class="comment outline icon"></i>Comments</a></div></div><div class="pushable" style="overflow: hidden;"><div id="scrollableDiv" class="problems_left_section__content__N0OKr problems_left_section__content_padding__qEUVv"><div class="pusher"><div class="undefined "><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Allocate Minimum Pages</h3><div style="padding-top: 2px;"><div class="sprint_sprint_popup_container__zCU0K"><i aria-hidden="true" class="bookmark outline icon"></i></div><div class="sprint_sprint_modal_container_mobile__09_Vr"><i aria-hidden="true" class="bookmark outline icon"></i></div></div></div><i id="bug_1" aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span>Difficulty: <strong>Medium</strong></span><span>Accuracy: <strong>35.51%</strong></span><span>Submissions: <strong>272K+</strong></span><span>Points: <strong>4</strong></span><span class="problems_label__MY7nU">Average Time: <strong>35m</strong></span></div><div class="ui divider"></div><div><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given an array <code>arr[]</code> of integers, where each element <code>arr[i]</code> represents the number of pages in the ith book. You also have an integer <code>k</code> representing the number of students. The task is to allocate books to each student such that:</span></p>
<ul>
<li><span style="font-size: 14pt;">Each student receives <strong>atleast</strong> one book.</span></li>
<li><span style="font-size: 14pt;">Each student is assigned a contiguous sequence of books.</span></li>
<li><span style="font-size: 14pt;">No book is assigned to more than one student.</span></li>
</ul>
<p><span style="font-size: 14pt;">The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.</span></p>
<p><span style="font-size: 18px;"><strong>Note</strong>: Return <strong>-1</strong> if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [12, 34, 67, 90], k = 2
<strong>Output: </strong>113
<strong>Explanation: </strong>Allocation can be done in following ways:
[12] and [34, 67, 90] Maximum Pages = 191
[12, 34] and [67, 90] Maximum Pages = 157
[12, 34, 67] and [90] Maximum Pages = 113.
Therefore, the minimum of these cases is 113, which is selected as the output.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [15, 17, 20], k = 5
<strong>Output: </strong>-1
<strong>Explanation: </strong>Allocation can not be done.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [22, 23, 67], k = 1
<strong>Output: </strong>112</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;=&nbsp; arr.size() &lt;= 10<sup>6</sup><br>1 &lt;= arr[i] &lt;= 10<sup>3<br></sup></span><span style="font-size: 18px;">1 &lt;= k &lt;= 10<sup>3&nbsp;</sup></span></p></div></div><div class="problems_problem_description_links__045ME"><button class="ui button">Try more examples</button></div><div class="accordion ui problems_accordion_tags_container__zk2Um"><div class="problems_accordion_tags__JJ2DX "><div class="title problems_active_tag_title__cgl9e"><div class="problems_tag_container__kWANg"><strong>Expected Complexities</strong><button class="ui mini circular button problems_tag_dropdown__x6C2I "><img src="./Allocate Minimum Pages _ op_files/Vector_1743491619.png" alt="Dropdown Icon"></button></div></div><div class="content animated_content closed"><div class="problems_expected_complexities_text__h_eyi"><div class="problems_normal_text__QiKrb">Time Complexity: O(n log n)</div><div class="problems_normal_text__QiKrb">Auxiliary Space: O(1)</div></div></div><div class="ui divider g-mt-3"></div></div><div class="problems_accordion_tags__JJ2DX problems_active_tags__3RExF"><div class="active title problems_active_tag_title__cgl9e"><div class="problems_tag_container__kWANg"><strong>Company Tags</strong><button class="ui mini circular button problems_tag_dropdown__x6C2I problems_rotate__oQqED"><img src="./Allocate Minimum Pages _ op_files/Vector_1743491619.png" alt="Dropdown Icon"></button></div></div><div class="content active animated_content open"><div class="ui labels"><a href="https://www.geeksforgeeks.org/explore?company[]=Infosys" target="_blank" class="ui label problems_tag_label__A4Ism">Infosys</a><a href="https://www.geeksforgeeks.org/explore?company[]=Amazon" target="_blank" class="ui label problems_tag_label__A4Ism">Amazon</a><a href="https://www.geeksforgeeks.org/explore?company[]=Microsoft" target="_blank" class="ui label problems_tag_label__A4Ism">Microsoft</a><a href="https://www.geeksforgeeks.org/explore?company[]=Google" target="_blank" class="ui label problems_tag_label__A4Ism">Google</a><a href="https://www.geeksforgeeks.org/explore?company[]=Codenation" target="_blank" class="ui label problems_tag_label__A4Ism">Codenation</a><a href="https://www.geeksforgeeks.org/explore?company[]=Uber" target="_blank" class="ui label problems_tag_label__A4Ism">Uber</a></div></div></div><div class="problems_accordion_tags__JJ2DX "><div class="title problems_active_tag_title__cgl9e"><div class="problems_tag_container__kWANg"><strong>Topic Tags</strong><button class="ui mini circular button problems_tag_dropdown__x6C2I "><img src="./Allocate Minimum Pages _ op_files/Vector_1743491619.png" alt="Dropdown Icon"></button></div></div><div class="content animated_content closed"><div class="ui labels"><a href="https://www.geeksforgeeks.org/explore?category[]=Searching" target="_blank" class="ui label problems_tag_label__A4Ism">Searching</a><a href="https://www.geeksforgeeks.org/explore?category[]=Divide%20and%20Conquer" target="_blank" class="ui label problems_tag_label__A4Ism">Divide and Conquer</a><a href="https://www.geeksforgeeks.org/explore?category[]=Algorithms" target="_blank" class="ui label problems_tag_label__A4Ism">Algorithms</a></div></div></div><div class="problems_accordion_tags__JJ2DX "><div class="title problems_active_tag_title__cgl9e"><div class="problems_tag_container__kWANg"><strong>Related Interview Experiences</strong><button class="ui mini circular button problems_tag_dropdown__x6C2I "><img src="./Allocate Minimum Pages _ op_files/Vector_1743491619.png" alt="Dropdown Icon"></button></div></div><div class="content animated_content closed"><div class="ui labels"><a href="https://www.geeksforgeeks.org/amazon-interview-experience-on-campus-for-sde-1-5/" target="_blank" class="ui label problems_tag_label__A4Ism">Amazon Interview Experience On Campus For Sde 1 5</a></div></div></div><div class="problems_accordion_tags__JJ2DX "><div class="title problems_active_tag_title__cgl9e"><div class="problems_tag_container__kWANg"><strong>Related Articles</strong><button class="ui mini circular button problems_tag_dropdown__x6C2I "><img src="./Allocate Minimum Pages _ op_files/Vector_1743491619.png" alt="Dropdown Icon"></button></div></div><div class="content animated_content closed"><div class="ui labels"><a href="https://www.geeksforgeeks.org/allocate-minimum-number-pages/" target="_blank" class="ui label problems_tag_label__A4Ism">Allocate Minimum Number Pages</a></div></div></div></div></div><div style="display: none;"><div class="comment_container" dark-mode="false"><section id="comment-sys"><div class="top_container"><div class="top_container__contents"><div class="left"><span class="title">Discussions</span><span class="threads"> ( 467 Threads )</span><a target="_blank" rel="noreferrer" class="redirection" href="https://discuss.geeksforgeeks.org/dashboard?utm-source=practice&amp;utm-event=comment-thread"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M13.6023 0.644922C13.5679 0.56187 13.5098 0.490857 13.4351 0.440858C13.3604 0.390859 13.2726 0.364118 13.1827 0.364014H7.72818C7.60763 0.364014 7.49202 0.411903 7.40677 0.497147C7.32153 0.58239 7.27364 0.698006 7.27364 0.818558C7.27364 0.939111 7.32153 1.05473 7.40677 1.13997C7.49202 1.22521 7.60763 1.2731 7.72818 1.2731H12.0855L6.04319 7.31537C5.99977 7.3573 5.96514 7.40745 5.94132 7.46291C5.9175 7.51837 5.90496 7.57801 5.90444 7.63837C5.90391 7.69872 5.91541 7.75857 5.93827 7.81444C5.96112 7.8703 5.99487 7.92105 6.03755 7.96373C6.08023 8.00641 6.13098 8.04016 6.18684 8.06301C6.24271 8.08587 6.30256 8.09737 6.36291 8.09684C6.42327 8.09632 6.48291 8.08378 6.53837 8.05996C6.59383 8.03613 6.64398 8.00151 6.68591 7.95809L12.7282 1.91583V6.2731C12.7282 6.39365 12.7761 6.50926 12.8613 6.59451C12.9466 6.67975 13.0622 6.72764 13.1827 6.72764C13.3033 6.72764 13.4189 6.67975 13.5041 6.59451C13.5894 6.50926 13.6373 6.39365 13.6373 6.2731V0.818558C13.637 0.758956 13.6251 0.69998 13.6023 0.644922Z" fill="#6E6E73"></path><path d="M11.0454 6.63607C10.9369 6.63607 10.8329 6.67917 10.7562 6.75589C10.6794 6.83261 10.6363 6.93666 10.6363 7.04516V12.3044C10.6361 12.537 10.5437 12.7599 10.3792 12.9244C10.2148 13.0888 9.99181 13.1813 9.75926 13.1815H1.69527C1.46272 13.1813 1.23975 13.0888 1.07531 12.9244C0.910874 12.7599 0.818397 12.537 0.818181 12.3044V4.24044C0.818397 4.00788 0.910874 3.78492 1.07531 3.62048C1.23975 3.45604 1.46272 3.36356 1.69527 3.36335H6.95453C7.06303 3.36335 7.16709 3.32025 7.2438 3.24353C7.32052 3.16681 7.36362 3.06275 7.36362 2.95426C7.36362 2.84576 7.32052 2.74171 7.2438 2.66499C7.16709 2.58827 7.06303 2.54517 6.95453 2.54517H1.69527C1.24579 2.5456 0.814843 2.72435 0.497012 3.04218C0.179181 3.36001 0.000433235 3.79096 0 4.24044V12.3044C0.000433235 12.7539 0.179181 13.1848 0.497012 13.5027C0.814843 13.8205 1.24579 13.9993 1.69527 13.9997H9.75926C10.2087 13.9993 10.6397 13.8205 10.9575 13.5027C11.2753 13.1848 11.4541 12.7539 11.4545 12.3044V7.04516C11.4545 6.93666 11.4114 6.83261 11.3347 6.75589C11.258 6.67917 11.1539 6.63607 11.0454 6.63607Z" fill="#6E6E73"></path></svg></a></div><div class="right"><div class="dropdown"><div class="action"><button class="filters_dropdown dropdown_toggle__btn" type="button"><span>Most Recent</span><span class="normal dropdown_icon"><svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2.5 3.75L5 6.25L7.5 3.75" stroke="#0E0E12" stroke-linecap="round" stroke-linejoin="round"></path></svg></span></button></div></div></div></div><div class="editor_container"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"><div class="editor_content"><div style="display: block;"><textarea id="prob701723" style="display: none;" aria-hidden="true"></textarea><div role="application" class="tox tox-tinymce" aria-disabled="false" style="visibility: hidden; height: 115px;" data-mce-style="visibility: hidden; height: 115px;"><div class="tox-editor-container"><div data-alloy-vertical-dir="toptobottom" class="tox-editor-header"><div role="group" class="tox-toolbar-overlord" aria-disabled="false"><div role="group" class="tox-toolbar__primary"><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button aria-label="Heading format" title="Heading format" aria-haspopup="true" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-expanded="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path fill-rule="evenodd" d="M17 5a1 1 0 010 2h-4v11a1 1 0 01-2 0V7H7a1 1 0 110-2h10z"></path></svg></span></button></div><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button aria-label="Bold" title="Bold" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M7.8 19c-.3 0-.5 0-.6-.2l-.2-.5V5.7c0-.2 0-.4.2-.5l.6-.2h5c1.5 0 2.7.3 3.5 1 .7.6 1.1 1.4 1.1 2.5a3 3 0 01-.6 1.9c-.4.6-1 1-1.6 1.2.4.1.9.3 1.3.6s.8.7 1 1.2c.4.4.5 1 .5 1.6 0 1.3-.4 2.3-1.3 3-.8.7-2.1 1-3.8 1H7.8zm5-8.3c.6 0 1.2-.1 1.6-.5.4-.3.6-.7.6-1.3 0-1.1-.8-1.7-2.3-1.7H9.3v3.5h3.4zm.5 6c.7 0 1.3-.1 1.7-.4.4-.4.6-.9.6-1.5s-.2-1-.7-1.4c-.4-.3-1-.4-2-.4H9.4v3.8h4z" fill-rule="evenodd"></path></svg></span></button><button aria-label="Italic" title="Italic" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M16.7 4.7l-.1.9h-.3c-.6 0-1 0-1.4.3-.3.3-.4.6-.5 1.1l-2.1 9.8v.6c0 .5.4.8 1.4.8h.2l-.2.8H8l.2-.8h.2c1.1 0 1.8-.5 2-1.5l2-9.8.1-.5c0-.6-.4-.8-1.4-.8h-.3l.2-.9h5.8z" fill-rule="evenodd"></path></svg></span></button><button aria-label="Underline" title="Underline" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M16 5c.6 0 1 .4 1 1v5.5a4 4 0 01-.4 1.8l-1 1.4a5.3 5.3 0 01-5.5 1 5 5 0 01-1.6-1c-.5-.4-.8-.9-1.1-1.4a4 4 0 01-.4-1.8V6c0-.6.4-1 1-1s1 .4 1 1v5.5c0 .3 0 .6.2 1l.6.7a3.3 3.3 0 002.2.8 3.4 3.4 0 002.2-.8c.3-.2.4-.5.6-.8l.2-.9V6c0-.6.4-1 1-1zM8 17h8c.6 0 1 .4 1 1s-.4 1-1 1H8a1 1 0 010-2z" fill-rule="evenodd"></path></svg></span></button></div><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button aria-label="Insert/edit link" title="Insert/edit link" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M6.2 12.3a1 1 0 011.4 1.4l-2.1 2a2 2 0 102.7 2.8l4.8-4.8a1 1 0 000-1.4 1 1 0 111.4-1.3 2.9 2.9 0 010 4L9.6 20a3.9 3.9 0 01-5.5-5.5l2-2zm11.6-.6a1 1 0 01-1.4-1.4l2-2a2 2 0 10-2.6-2.8L11 10.3a1 1 0 000 1.4A1 1 0 119.6 13a2.9 2.9 0 010-4L14.4 4a3.9 3.9 0 015.5 5.5l-2 2z" fill-rule="nonzero"></path></svg></span></button><button aria-label="Insert/edit code sample" title="Insert/edit code sample" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="26" focusable="false"><path d="M7.1 11a2.8 2.8 0 01-.8 2 2.8 2.8 0 01.8 2v1.7c0 .3.1.6.4.8.2.3.5.4.8.4.3 0 .4.2.4.4v.8c0 .2-.1.4-.4.4-.7 0-1.4-.3-2-.8-.5-.6-.8-1.3-.8-2V15c0-.3-.1-.6-.4-.8-.2-.3-.5-.4-.8-.4a.4.4 0 01-.4-.4v-.8c0-.2.2-.4.4-.4.3 0 .6-.1.8-.4.3-.2.4-.5.4-.8V9.3c0-.7.3-1.4.8-2 .6-.5 1.3-.8 2-.8.3 0 .4.2.4.4v.8c0 .2-.1.4-.4.4-.3 0-.6.1-.8.4-.3.2-.4.5-.4.8V11zm9.8 0V9.3c0-.3-.1-.6-.4-.8-.2-.3-.5-.4-.8-.4a.4.4 0 01-.4-.4V7c0-.2.1-.4.4-.4.7 0 1.4.3 2 .8.5.6.8 1.3.8 2V11c0 .3.1.6.4.8.2.3.5.4.8.4.2 0 .4.2.4.4v.8c0 .2-.2.4-.4.4-.3 0-.6.1-.8.4-.3.2-.4.5-.4.8v1.7c0 .7-.3 1.4-.8 2-.6.5-1.3.8-2 .8a.4.4 0 01-.4-.4v-.8c0-.2.1-.4.4-.4.3 0 .6-.1.8-.4.3-.2.4-.5.4-.8V15a2.8 2.8 0 01.8-2 2.8 2.8 0 01-.8-2zm-3.3-.4c0 .4-.1.8-.5 1.1-.3.3-.7.5-1.1.5-.4 0-.8-.2-1.1-.5-.4-.3-.5-.7-.5-1.1 0-.5.1-.9.5-1.2.3-.3.7-.4 1.1-.4.4 0 .8.1 1.1.4.4.3.5.7.5 1.2zM12 13c.4 0 .8.1 1.1.5.4.3.5.7.5 1.1 0 1-.1 1.6-.5 2a3 3 0 01-1.1 1c-.4.3-.8.4-1.1.4a.5.5 0 01-.5-.5V17a3 3 0 001-.2l.6-.6c-.6 0-1-.2-1.3-.5-.2-.3-.3-.7-.3-1 0-.5.1-1 .5-1.2.3-.4.7-.5 1.1-.5z" fill-rule="evenodd"></path></svg></span></button><button aria-label="Insert Image" title="Insert Image" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M5 15.7l3.3-3.2c.3-.3.7-.3 1 0L12 15l4.1-4c.3-.4.8-.4 1 0l2 1.9V5H5v10.7zM5 18V19h3l2.8-2.9-2-2L5 17.9zm14-3l-2.5-2.4-6.4 6.5H19v-4zM4 3h16c.6 0 1 .4 1 1v16c0 .6-.4 1-1 1H4a1 1 0 01-1-1V4c0-.6.4-1 1-1zm6 8a2 2 0 100-4 2 2 0 000 4z" fill-rule="nonzero"></path></svg></span></button></div><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button aria-label="Bullet list" title="Bullet list" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M11 5h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 010-2zm0 6h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 010-2zm0 6h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 010-2zM4.5 6c0-.4.1-.8.4-1 .3-.4.7-.5 1.1-.5.4 0 .8.1 1 .4.4.3.5.7.5 1.1 0 .4-.1.8-.4 1-.3.4-.7.5-1.1.5-.4 0-.8-.1-1-.4-.4-.3-.5-.7-.5-1.1zm0 6c0-.4.1-.8.4-1 .3-.4.7-.5 1.1-.5.4 0 .8.1 1 .4.4.3.5.7.5 1.1 0 .4-.1.8-.4 1-.3.4-.7.5-1.1.5-.4 0-.8-.1-1-.4-.4-.3-.5-.7-.5-1.1zm0 6c0-.4.1-.8.4-1 .3-.4.7-.5 1.1-.5.4 0 .8.1 1 .4.4.3.5.7.5 1.1 0 .4-.1.8-.4 1-.3.4-.7.5-1.1.5-.4 0-.8-.1-1-.4-.4-.3-.5-.7-.5-1.1z" fill-rule="evenodd"></path></svg></span></button><button aria-label="Numbered list" title="Numbered list" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false" aria-pressed="false"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M10 17h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 010-2zm0-6h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 010-2zm0-6h8c.6 0 1 .4 1 1s-.4 1-1 1h-8a1 1 0 110-2zM6 4v3.5c0 .3-.2.5-.5.5a.5.5 0 01-.5-.5V5h-.5a.5.5 0 010-1H6zm-1 8.8l.2.2h1.3c.3 0 .5.2.5.5s-.2.5-.5.5H4.9a1 1 0 01-.9-1V13c0-.4.3-.8.6-1l1.2-.4.2-.3a.2.2 0 00-.2-.2H4.5a.5.5 0 01-.5-.5c0-.3.2-.5.5-.5h1.6c.5 0 .9.4.9 1v.1c0 .4-.3.8-.6 1l-1.2.4-.2.3zM7 17v2c0 .6-.4 1-1 1H4.5a.5.5 0 010-1h1.2c.2 0 .3-.1.3-.3 0-.2-.1-.3-.3-.3H4.4a.4.4 0 110-.8h1.3c.2 0 .3-.1.3-.3 0-.2-.1-.3-.3-.3H4.5a.5.5 0 110-1H6c.6 0 1 .4 1 1z" fill-rule="evenodd"></path></svg></span></button></div><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button aria-label="Undo" title="Undo" type="button" tabindex="-1" class="tox-tbtn tox-tbtn--disabled" aria-disabled="true"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M6.4 8H12c3.7 0 6.2 2 6.8 5.1.6 2.7-.4 5.6-2.3 6.8a1 1 0 01-1-1.8c1.1-.6 1.8-2.7 1.4-4.6-.5-2.1-2.1-3.5-4.9-3.5H6.4l3.3 3.3a1 1 0 11-1.4 1.4l-5-5a1 1 0 010-1.4l5-5a1 1 0 011.4 1.4L6.4 8z" fill-rule="nonzero"></path></svg></span></button><button aria-label="Redo" title="Redo" type="button" tabindex="-1" class="tox-tbtn tox-tbtn--disabled" aria-disabled="true"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path d="M17.6 10H12c-2.8 0-4.4 1.4-4.9 3.5-.4 2 .3 4 1.4 4.6a1 1 0 11-1 1.8c-2-1.2-2.9-4.1-2.3-6.8.6-3 3-5.1 6.8-5.1h5.6l-3.3-3.3a1 1 0 111.4-1.4l5 5a1 1 0 010 1.4l-5 5a1 1 0 01-1.4-1.4l3.3-3.3z" fill-rule="nonzero"></path></svg></span></button></div><div title="" role="toolbar" data-alloy-tabstop="true" tabindex="-1" class="tox-toolbar__group"><button title="Table" aria-label="Table" aria-haspopup="true" type="button" tabindex="-1" data-alloy-tabstop="true" unselectable="on" class="tox-tbtn tox-tbtn--select" aria-expanded="false" style="user-select: none;"><span class="tox-icon tox-tbtn__icon-wrap"><svg width="24" height="24" focusable="false"><path fill-rule="nonzero" d="M19 4a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V6c0-1.1.9-2 2-2h14zM5 14v4h6v-4H5zm14 0h-6v4h6v-4zm0-6h-6v4h6V8zM5 12h6V8H5v4z"></path></svg></span><div class="tox-tbtn__select-chevron"><svg width="10" height="10" focusable="false"><path d="M8.7 2.2c.3-.3.8-.3 1 0 .4.4.4.9 0 1.2L5.7 7.8c-.3.3-.9.3-1.2 0L.2 3.4a.8.8 0 010-1.2c.3-.3.8-.3 1.1 0L5 6l3.7-3.8z" fill-rule="nonzero"></path></svg></div></button></div></div></div><div class="tox-anchorbar"></div></div><div class="tox-sidebar-wrap"><div class="tox-edit-area"><iframe id="prob701723_ifr" frameborder="0" allowtransparency="true" title="Rich Text Area" class="tox-edit-area__iframe" src="./Allocate Minimum Pages _ op_files/saved_resource.html"></iframe></div><div role="complementary" class="tox-sidebar"><div data-alloy-tabstop="true" tabindex="-1" class="tox-sidebar__slider tox-sidebar--sliding-closed" style="width: 0px;"><div class="tox-sidebar__pane-container"></div></div></div></div></div><div aria-hidden="true" class="tox-throbber" style="display: none;"></div></div></div><div class="action_buttons"><span class="commenting_as">Commenting as <b>Heena</b></span><input type="checkbox" class="anonymous_checkbox"><span class="anonymous_comment_label">Comment Anonymously</span><button disabled="" class="submit_btn btn green ">Submit<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M15.8324 10.1454H6.66569" stroke="#9597A1" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15.8333 10.1458L4.58325 15.2917L6.66659 10.1458L4.58325 5L15.8333 10.1458Z" stroke="#9597A1" stroke-linecap="round" stroke-linejoin="round"></path></svg></span></button></div></div></div></div><div class="bottom_container"><div class="bottom_contents"><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><span class="user_name">GeeksforGeeks<img class="" title="GFG Team" src="./Allocate Minimum Pages _ op_files/0b794caf-1192-4364-839d-a9f6f3f20107_1686651794.svg" alt="verified"></span><span class="user_time">5 months ago<span class="user_time_details">Dec 18, 2024 09:31 (GMT +5:30)</span></span><span class="pinned_image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M7.85087 12.1491L10.307 14.6053L11.0265 13.8859C11.3521 13.5602 11.5351 13.1185 11.5351 12.6578V10.921L13.9913 8.46496L15.8334 7.85088L12.1491 4.16663L11.535 6.00873L9.07896 8.46488H7.34221C6.88154 8.46488 6.43987 8.64788 6.11413 8.97354L5.39471 9.69296L7.85087 12.1491ZM7.85087 12.1491L4.16671 15.8333L7.85087 12.1491Z" fill="#357960"></path><path d="M7.85087 12.1491L10.307 14.6053L11.0265 13.8859C11.3521 13.5602 11.5351 13.1185 11.5351 12.6578V10.921L13.9913 8.46496L15.8334 7.85088L12.1491 4.16663L11.535 6.00873L9.07896 8.46488H7.34221C6.88154 8.46488 6.43987 8.64788 6.11412 8.97354L5.39471 9.69296L7.85087 12.1491ZM7.85087 12.1491L4.16671 15.8333" stroke="#357960" stroke-linecap="round" stroke-linejoin="round"></path></svg></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p><strong>We are Hiring: DSA Mentor Intern!</strong></p>
<ul>
<li>We are Looking for a talented and motivated DSA Mentor Intern to join our team.</li>
<li>Please fill the&nbsp;<strong>form&nbsp;</strong>to complete your application.<br><br>https://docs.google.com/forms/d/e/1FAIpQLSfMPSG2PlQUjUuAFbTAw0fti5kqqzlmqrxjrw8cTHpHjfVbfA/viewform</li>
</ul></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>5</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/thisisnitish/practice/" target="_blank" rel="noreferrer" class="user_name">Nitish Kumar</a><span class="user_time">1 week ago<span class="user_time_details">May 12, 2025 20:51 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><pre class="language-cpp"><code>class Solution 
{
    public:
    bool isValid(int arr[], int sz, int maxPages, int M){
        int student = 1, pages = 0;
        
        for(int i=0; i&lt;sz; i++){
            pages += arr[i];
            if(pages &gt; maxPages){
                pages = arr[i];
                student++;
            }
            
            if(student &gt; M ) return false;
        }
        
        if(student &gt; M) return false;
        return true;
    }
    
    //Function to find minimum number of pages.
    int findPages(int A[], int N, int M) 
    {
        if(N &lt; M) return -1;
        int low = INT_MIN, high = 0;
        for(int i=0; i&lt;N; i++){
            low = max(low, A[i]);
            high += A[i];
        }
        
        int res = -1;
        
        while(low &lt;= high){
            int mid = low + (high - low) / 2;
            
            if(isValid(A, N, mid, M)){
                res = mid;
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
        
        return res;
    }
};</code></pre>
<p>&nbsp;</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/bhavishya_12u/practice/" target="_blank" rel="noreferrer" class="user_name">Bhavishya Goyal</a><span class="user_time">2 weeks ago<span class="user_time_details">May 04, 2025 00:16 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p>// Java Code , with comments to explain working of code</p>
<p>class Solution {<br>&nbsp; &nbsp; public static int findPages(int[] arr, int k) {<br>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;if(k&gt;arr.length)return -1; &nbsp; &nbsp;// agar students books se zyada hain to allocation possible nahi hai<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;int start=Integer.MIN_VALUE; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;int end=0; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;for(int i=0;i&lt;arr.length;i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;start=Math.max(start,arr[i]); // sabse zyada pages wali book dhundh rahe hain<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;end+=arr[i]; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // total pages ka sum nikal rahe hain<br>&nbsp; &nbsp; &nbsp; &nbsp;};<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;int ans=-1;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;// binary search karenge max pages ke liye<br>&nbsp; &nbsp; &nbsp; &nbsp;// start = max book pages, end = total sum of pages<br>&nbsp; &nbsp; &nbsp; &nbsp;while(start&lt;=end){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;int mid= start+(end-start)/2; &nbsp;// mid = max pages ka guess</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;int pages=0;int count=1; &nbsp; &nbsp; &nbsp; // pages = current student ke pages, count = student count<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for(int i=0;i&lt;arr.length;i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pages+=arr[i]; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // current book add karo</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(pages&gt;mid){ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// agar limit cross ho gayi<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pages=arr[i]; &nbsp; &nbsp; &nbsp; &nbsp; // naye student ke pages reset<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;count++; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// naye student ko assign kiya<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(count&lt;=k){ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // agar k ya usse kam students me ho gaya<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ans=mid; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// ye valid answer ho sakta hai<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;end=mid-1; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// aur kam pages try karo<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;start=mid+1; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// students zyada lage, pages limit badhao<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp;}</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;return ans;<br>&nbsp; &nbsp; }<br>}</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>2</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div><div class="show_reply__container"><a target="#threads_comment_da792eb0-7eb4-426e-b6a0-68a3ab71750c">(Show 2 Replies)</a></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/souvikkarmakar2k19/practice/" target="_blank" rel="noreferrer" class="user_name">Souvik Karmakar</a><span class="user_time">3 weeks ago<span class="user_time_details">Apr 28, 2025 12:36 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p>Use BS on answer .</p>
<p>TC -&gt; O(n * log(sum of (arr))</p>
<p>SC -&gt; O(1)</p>
<p>Intuition :</p>
<ul>
<li>We need to use BS on ans -&gt; We need to find min(max of pages)</li>
<li>To figure out the range : start = Max(arr) and end = Sum(arr) [because , if one student is assigned , then that student should be able to read all the pages | | | | the end is sum because lets say only one student is allocated all the pages .</li>
<li>Function Definition : isAllocationPossible -&gt; We check for 1st student that how many pages can be assigned limit to pageLimit , If it exceeds , then we need to increment the studentCount . AT the end we check if the studentCount &lt;= students(given in ques)</li>
</ul>
<p>Approach :</p>
<ul>
<li>We figure out the range by calculating the start and end&nbsp;</li>
<li>We take account of an edge case , that if number of books is &lt; students , then return -1</li>
<li>We calculate the mid</li>
<li>If the function isAllocationPossible is valid , then we go ahead and search in the left half , else , we search in the right half . &nbsp;</li>
</ul>
<p>&nbsp;</p>
<p>Code :&nbsp;</p>
<pre class="language-java"><code>class Solution {
    public static int findPages(int[] arr, int k) {
        // code here
        if(arr.length &lt; k) return -1;
        int start = Integer.MIN_VALUE;
        int end = 0;
        for(int i : arr) {
            start = Math.max(start, i);
            end += i;
        }
        int ans = -1;
        while(start &lt;= end) {
            int mid = start + (end-start)/2;
            if(isAllocationPossible(arr, k, mid)) {
                ans = mid;
                end = mid-1;
            } else {
                start = mid+1;
            }
        }
        return ans;
    }
    
    public static boolean isAllocationPossible(int[] arr, int students, int pageLimit) {
        int pages = 0;
        int studentCount = 1;
        for(int i : arr) {
            pages += i;
            if(pages &gt; pageLimit) {
                studentCount++;
                pages = i;
            }
        }
        return studentCount &lt;= students;
    }
}</code></pre>
<p>&nbsp;</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/kprafullya35/practice/" target="_blank" rel="noreferrer" class="user_name">Prafull Kumar Yadav</a><span class="user_time">4 weeks ago<span class="user_time_details">Apr 25, 2025 22:38 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p>Brute Force Solution is :</p>
<p>&nbsp;</p>
<p>//{ Driver Code Starts<br>// Initial function template for C++</p>
<p>#include &lt;bits/stdc++.h&gt;<br>using namespace std;</p>
<p><br>// } Driver Code Ends</p>
<p>class Solution {<br>&nbsp; public:<br>&nbsp;&nbsp;<br>&nbsp;&nbsp;<br>&nbsp;&nbsp;<br>&nbsp; &nbsp;int countPages(vector&lt;int&gt; &amp;arr, int i){<br>&nbsp; &nbsp; &nbsp; &nbsp;int n=arr.size();<br>&nbsp; &nbsp; &nbsp; &nbsp;int pagesSum=0;<br>&nbsp; &nbsp; &nbsp; &nbsp;int Stucount=1;<br>&nbsp; &nbsp; &nbsp; &nbsp;for(int j=0;j&lt;n;j++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(pagesSum+arr[j]&lt;=i){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pagesSum+=arr[j];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Stucount++;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pagesSum=arr[j];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;return Stucount;<br>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp;}<br>&nbsp; &nbsp;<br>&nbsp; &nbsp; int findPages(vector&lt;int&gt; &amp;arr, int k) {<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; int ans= INT_MAX;<br>&nbsp; &nbsp; &nbsp; &nbsp; // code here<br>&nbsp; &nbsp; int low = *max_element(arr.begin(), arr.end());<br>&nbsp; &nbsp; int high = accumulate(arr.begin(), arr.end(), 0);<br>&nbsp; &nbsp; int n=arr.size();<br>&nbsp; &nbsp; if(k&gt;n){<br>&nbsp; &nbsp; &nbsp; &nbsp; return -1;<br>&nbsp; &nbsp; }<br>&nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; for(int i=low; i&lt;=high;i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; int nopages = countPages(arr,i);<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; if(nopages==k){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return i;<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; }<br>&nbsp; &nbsp;return low;<br>&nbsp; &nbsp; }<br>};</p>
<p><br>//{ Driver Code Starts.</p>
<p>int main() {<br>&nbsp; &nbsp; int test_case;<br>&nbsp; &nbsp; cin &gt;&gt; test_case;<br>&nbsp; &nbsp; cin.ignore();<br>&nbsp; &nbsp; while (test_case--) {</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; int d;<br>&nbsp; &nbsp; &nbsp; &nbsp; vector&lt;int&gt; arr, brr, crr;<br>&nbsp; &nbsp; &nbsp; &nbsp; string input;<br>&nbsp; &nbsp; &nbsp; &nbsp; getline(cin, input);<br>&nbsp; &nbsp; &nbsp; &nbsp; stringstream ss(input);<br>&nbsp; &nbsp; &nbsp; &nbsp; int number;<br>&nbsp; &nbsp; &nbsp; &nbsp; while (ss &gt;&gt; number) {<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; arr.push_back(number);<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; getline(cin, input);<br>&nbsp; &nbsp; &nbsp; &nbsp; ss.clear();<br>&nbsp; &nbsp; &nbsp; &nbsp; ss.str(input);<br>&nbsp; &nbsp; &nbsp; &nbsp; while (ss &gt;&gt; number) {<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; crr.push_back(number);<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; d = crr[0];<br>&nbsp; &nbsp; &nbsp; &nbsp; int n = arr.size();<br>&nbsp; &nbsp; &nbsp; &nbsp; Solution ob;<br>&nbsp; &nbsp; &nbsp; &nbsp; int ans = ob.findPages(arr, d);<br>&nbsp; &nbsp; &nbsp; &nbsp; cout &lt;&lt; ans &lt;&lt; endl;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; cout &lt;&lt; "~"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;&lt; "\n";<br>&nbsp; &nbsp; }<br>&nbsp; &nbsp; return 0;<br>}<br>// } Driver Code Ends</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/routyash7/practice/" target="_blank" rel="noreferrer" class="user_name">Yashwant Rout</a><span class="user_time">1 month ago<span class="user_time_details">Apr 22, 2025 09:09 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p>in questions it is mentioned we need to allocate atleast one book to k students ,&nbsp;<br>but solutions works when studentcount&lt;k.<br>RIP Desccription.<br><br></p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>2</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div><div class="show_reply__container"><a target="#threads_comment_33ec6cf5-9556-4058-a579-c48babf979ee">(Show 1 Replies)</a></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/dhiraj1002/practice/" target="_blank" rel="noreferrer" class="user_name">Dhiraj Gupta</a><span class="user_time">1 month ago<span class="user_time_details">Apr 20, 2025 13:37 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><ul>
<li>C++ || optimized || BS on answers</li>
</ul>
<p>class Solution {<br>&nbsp; public:<br>&nbsp; int isPossible(vector&lt;int&gt; &amp;pages, int m, int maxPages){<br>&nbsp; &nbsp; &nbsp; int studentCount = 1;<br>&nbsp; &nbsp; &nbsp; int currentPages = 0;<br>&nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; for(int i=0;i&lt;pages.size();i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(pages[i]&gt;maxPages) return false;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(currentPages + pages[i] &gt; maxPages){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; studentCount++;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; currentPages =pages[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (studentCount &gt; m) return false;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else {<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;currentPages += pages[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; return true ;<br>&nbsp; }&nbsp;<br>&nbsp;&nbsp;<br>&nbsp;&nbsp;<br>&nbsp; &nbsp; int findPages(vector&lt;int&gt; &amp;pages, int m) {<br>&nbsp; &nbsp; &nbsp; &nbsp; if(pages.size() &lt; m) return -1 ;<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; int low = *max_element(pages.begin(),pages.end());<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; int high = accumulate(pages.begin(), pages.end(),0);<br>&nbsp; &nbsp; &nbsp; &nbsp; int result = high;<br>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; while(low&lt;=high){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; int mid = low + (high-low)/2;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(isPossible(pages,m,mid)){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; result = mid;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; high = mid-1;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; low = mid + 1;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; return result ;<br>&nbsp; &nbsp; }<br>};</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><span class="user_name">Anonymous_Geek</span><span class="user_time">2 months ago<span class="user_time_details">Mar 18, 2025 07:17 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><p>class Solution {<br>&nbsp; public:<br>&nbsp; bool ispossible(vector&lt;int&gt; &amp;arr, int pages,int k){<br>&nbsp; &nbsp; &nbsp; int cnt=1;<br>&nbsp; &nbsp; &nbsp; int sum=0;<br>&nbsp; &nbsp; &nbsp; for(int i=0;i&lt;arr.size();i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(sum+arr[i]&lt;=pages){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;sum+=arr[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;cnt++;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(cnt&gt;k || arr[i]&gt;pages){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return false;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;sum=arr[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}<br>&nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return true;<br>&nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; }<br>&nbsp; &nbsp; int findPages(vector&lt;int&gt; &amp;arr, int k) {<br>&nbsp; &nbsp; &nbsp; &nbsp; // code here<br>&nbsp; &nbsp; &nbsp; &nbsp; int left=*min_element(arr.begin(),arr.end());<br>&nbsp; &nbsp; &nbsp; &nbsp; int right=accumulate(arr.begin(),arr.end(),0);<br>&nbsp; &nbsp; &nbsp; &nbsp; if(k&gt;arr.size()){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return -1;<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; int ans=-1;<br>&nbsp; &nbsp; &nbsp; &nbsp; while(left&lt;=right){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; int mid=left+(right-left)/2;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(ispossible(arr,mid,k)){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ans=mid;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; right=mid-1;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; left=mid+1;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; return ans;<br>&nbsp; &nbsp; }<br>};</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/revan87013/practice/" target="_blank" rel="noreferrer" class="user_name">Gunaganti Revan Kumar</a><span class="user_time">3 months ago<span class="user_time_details">Feb 15, 2025 18:06 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><h1><strong>Java Optimal and Easy Solution</strong></h1>
<p>class Solution {<br>&nbsp; &nbsp; public static int findPages(int[] arr, int k) {<br>&nbsp; &nbsp; &nbsp; &nbsp; int n=arr.length;<br>&nbsp; &nbsp; &nbsp; &nbsp; if(k&gt;n)return -1;<br>&nbsp; &nbsp; &nbsp; &nbsp; int low=Integer.MIN_VALUE;<br>&nbsp; &nbsp; &nbsp; &nbsp; int high=0;<br>&nbsp; &nbsp; &nbsp; &nbsp; int ans=-1;<br>&nbsp; &nbsp; &nbsp; &nbsp; for(int i:arr){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; high+=i;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; low=Math.max(i,low);<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; while(low&lt;=high){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; int mid=(low+high)/2;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(possible(arr,mid,k)){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; high=mid-1;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ans=mid;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else low=mid+1;<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; return ans;<br>&nbsp; &nbsp; }<br>&nbsp; &nbsp; static boolean possible(int[] arr,int pages,int k){<br>&nbsp; &nbsp; &nbsp; &nbsp; int students=1;<br>&nbsp; &nbsp; &nbsp; &nbsp; int pagesStudent=0;<br>&nbsp; &nbsp; &nbsp; &nbsp; for(int i=0;i&lt;arr.length;i++){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(arr[i]+pagesStudent&lt;=pages){<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pagesStudent+=arr[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else{<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; students++;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pagesStudent=arr[i];<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if(students&gt;k)return false;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; }<br>&nbsp; &nbsp; &nbsp; &nbsp; return true;<br>&nbsp; &nbsp; }<br>}</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>1</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div><div class="single_comment"><div class="items"><div class="left"><img alt="User" src="./Allocate Minimum Pages _ op_files/user_web-1598433228.svg" class="user_image"></div><div class="right"><div class="meta"><div class="user_info"><a href="https://auth.geeksforgeeks.org/user/jainsakshi9301/practice/" target="_blank" rel="noreferrer" class="user_name">Sakshi</a><span class="user_time">3 months ago<span class="user_time_details">Feb 15, 2025 12:16 (GMT +5:30)</span></span></div><div class="dropdown"><div class="dropdown_content"><div class="dropdown"><div class="action"><button class="dropdown_toggle__btn" type="button"><span><svg width="2" height="8" viewBox="0 0 2 8" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="#9597A1"></circle><circle cx="1" cy="4" r="1" fill="#9597A1"></circle><circle cx="1" cy="7" r="1" fill="#9597A1"></circle></svg></span></button></div></div></div></div></div><div class="text"><div><h2>JAVA Code</h2>
<pre class="language-java"><code>class Solution {
    public static int findPages(int[] arr, int k) {
        if(k &gt; arr.length) return -1;
        
        int start = 0;
        int end = Arrays.stream(arr).sum();
        int ans = -1;
        
        while(start &lt;= end) { // Binary Search
            int mid = (start + end) / 2;
            
            if(isValid(mid, arr, k)) {
                ans = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        return ans;
    }
    
    public static boolean isValid(int maxPages, int[] arr, int k) {
        int studentCount = 1;
        int currPages = 0;
        
        for(int i=0; i&lt;arr.length; i++) {
            if(arr[i] &gt; maxPages) return false; // Edge case
            
            if(currPages + arr[i] &gt; maxPages) {
                studentCount++;
                currPages = arr[i];
            } else {
                currPages += arr[i];
            }
        }
        
        return (studentCount &lt;= k);
    }
}</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p></div></div><div class="read_container"></div><div class="bottom"><div class="voting_container"><div class="up_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9.60751 1.285C9.31111 0.905 8.68891 0.905 8.39251 1.285L2.16981 9.293C2.07851 9.411 2.02141 9.55299 2.00491 9.70199C1.98851 9.85199 2.01341 10.004 2.07681 10.14C2.14031 10.276 2.23971 10.39 2.36361 10.471C2.48751 10.551 2.63091 10.594 2.77731 10.594H5.88871V16.199C5.88871 16.412 5.97061 16.615 6.11641 16.765C6.26231 16.916 6.46021 17 6.66651 17H11.3335C11.5398 17 11.7377 16.916 11.8835 16.765C12.0294 16.615 12.1114 16.412 12.1114 16.199V10.594H15.2227C15.3691 10.594 15.5126 10.551 15.6364 10.471C15.7603 10.39 15.8597 10.276 15.9232 10.14C15.9866 10.004 16.0115 9.85199 15.9951 9.70199C15.9786 9.55299 15.9215 9.411 15.8302 9.293L9.60751 1.285Z" fill="#2F8D46"></path></svg></button><span>0</span></div><div class="down_votes"><button class=""><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M8.39249 16.715C8.68889 17.095 9.31109 17.095 9.60749 16.715L15.8302 8.707C15.9215 8.589 15.9786 8.44701 15.9951 8.29801C16.0115 8.14801 15.9866 7.996 15.9232 7.86C15.8597 7.724 15.7603 7.61001 15.6364 7.52901C15.5125 7.44901 15.3691 7.40601 15.2227 7.40601L12.1113 7.40601L12.1113 1.801C12.1113 1.588 12.0294 1.385 11.8836 1.235C11.7377 1.084 11.5398 1 11.3335 1L6.66649 1C6.46019 1 6.26229 1.08401 6.11649 1.23501C5.97059 1.385 5.88859 1.588 5.88859 1.801L5.88859 7.40601L2.77729 7.40601C2.63089 7.40601 2.48739 7.44901 2.36359 7.52901C2.23969 7.61001 2.14029 7.72401 2.07679 7.86001C2.01339 7.99601 1.98849 8.14801 2.00489 8.29801C2.02139 8.44701 2.07849 8.58901 2.16979 8.70701L8.39249 16.715Z" fill="#E02828"></path></svg></button></div></div><div class="replies_container"><div class="reply_container"><span style="cursor: pointer;">Reply</span></div></div></div></div></div></div></div><div class="load_more__comments"><button class="btn">Load More Comments</button></div></div></section></div></div><div class="problems_bottom_report_issue__oEbhU"><div class="reportIssueModal_report_issue_button__KoQ6r"><button class="ui yellow mini button"><i aria-hidden="true" class="bug icon"></i>Report An Issue</button><span>If you are facing any issue on this page. Please let us know.</span></div></div></div></div><div class="ui segment ui overlay bottom sidebar problems_output_window__G_LTH  problems_normal_height__Og1iy"><div class="problems_header__E09Dq"><h4>Output Window</h4><div class="problems_header_icons__h94Bp"><div class="problems_header_icon__4Wp8F"><svg xmlns="http://www.w3.org/2000/svg" width="18.2" height="1.2" viewBox="0 0 18.2 1.2"><line id="Line_419" data-name="Line 419" x2="17" transform="translate(0.6 0.6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-width="1.2"></line></svg></div><div class="problems_header_icon__4Wp8F"><svg id="Group_13529" data-name="Group 13529" xmlns="http://www.w3.org/2000/svg" width="29.906" height="29.906" viewBox="0 0 29.906 29.906" class="maximize_height"><path id="Path_16034" data-name="Path 16034" d="M0,0H29.906V29.906H0Z" fill="none" class="outer_path"></path><path id="Path_16035" data-name="Path 16035" d="M16,4h4.984V8.984" transform="translate(3.938 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_430" data-name="Line 430" y1="7" x2="7" transform="translate(17.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16036" data-name="Path 16036" d="M8.984,20.984H4V16" transform="translate(0.984 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_431" data-name="Line 431" y1="8" x2="8" transform="translate(4.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16037" data-name="Path 16037" d="M16,20.984h4.984V16" transform="translate(3.938 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_432" data-name="Line 432" x2="7" y2="8" transform="translate(17.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16038" data-name="Path 16038" d="M8.984,4H4V8.984" transform="translate(0.984 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_433" data-name="Line 433" x2="8" y2="7" transform="translate(4.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line></svg></div><div class="problems_header_icon__4Wp8F"><svg id="Group_8364" data-name="Group 8364" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path id="Path_7108" data-name="Path 7108" d="M0,0H24V24H0Z" fill="none" class="outer_path"></path><line id="Line_398" data-name="Line 398" x1="12" y2="12" transform="translate(6 6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"></line><line id="Line_399" data-name="Line 399" x2="12" y2="12" transform="translate(6 6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"></line></svg></div></div></div><div class="problems_content__I8YGa "><div class="ui green pointing secondary menu"><a class="item">Compilation Results</a><a class="item">Custom Input</a></div></div></div></div></div></div><div class="reflex-splitter"><div class="problems_split_div__cAR1M"><div class="problems_resize_icon__qM0Nd" style="background: url(&quot;https://media.geeksforgeeks.org/img-practice/slider-1655446161.png&quot;);"></div></div></div><div class="pane-content vertical reflex-element" style="flex: 0.5 1 0%;"><div class="problems_right_section__iOL26  " id="problem_right_section"><div class="problems_header__E09Dq"><div class="ui top attached tabular problems_header_menu__aKU8f menu"><div role="listbox" aria-expanded="false" class="ui selection dropdown problems_language_dropdown__DgjFb
            " tabindex="0"><div aria-atomic="true" aria-live="polite" role="alert" class="divider text">Python3</div><i aria-hidden="true" class="dropdown icon"></i><div class="menu transition"><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><span class="text">C (gcc 5.4)</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><span class="text">C++ (g++ 5.4)</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><span class="text">Java (1.8)</span></div><div role="option" aria-checked="true" aria-selected="true" class="active selected item" style="pointer-events: all;"><span class="text">Python3</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><span class="text">C#</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><span class="text">Javascript (Node v12.19.0)</span></div></div></div><div class="problems_add_notes_action_container__wK_fp"><div class="problems_problem_timer_content__24gPQ"><div class="problems_user_timer_div__AR0yn"><button id="start_timer" class="ui small compact icon button problems_user_timer_button__1fQzl"><div class="problems_user_timer_div__AR0yn"><svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="clock_timer"><g opacity="0.73"><path d="M7.1092 11.8489C9.39941 11.8489 11.256 9.99231 11.256 7.70209C11.256 5.41188 9.39941 3.5553 7.1092 3.5553C4.81899 3.5553 2.9624 5.41188 2.9624 7.70209C2.9624 9.99231 4.81899 11.8489 7.1092 11.8489Z" stroke="#FF9700" stroke-linecap="round" stroke-linejoin="round" class="outer_path"></path><path d="M7.10913 5.92444V7.70205H8.29372" stroke="#FF9700" stroke-linecap="round" stroke-linejoin="round" class="outer_path2"></path><path d="M4.14669 2.36914L2.51733 3.55373" stroke="#FF9700" stroke-linecap="round" stroke-linejoin="round" class="outer_path3"></path><path d="M10.071 2.36914L11.7004 3.55373" stroke="#FF9700" stroke-linecap="round" stroke-linejoin="round" class="outer_path4"></path></g></svg><span class="problems_user_start_timer_text__Wfv0I"> Start Timer </span><svg xmlns="http://www.w3.org/2000/svg" width="13.004" height="13.004" viewBox="0 0 13.004 13.004"><path id="play_circle_FILL0_wght400_GRAD0_opsz48" d="M8.925,13.265l4.34-2.763L8.925,7.739ZM10.5,17a6.291,6.291,0,0,1-2.52-.512,6.551,6.551,0,0,1-3.47-3.47,6.495,6.495,0,0,1,0-5.055A6.5,6.5,0,0,1,5.91,5.9a6.665,6.665,0,0,1,2.072-1.39,6.495,6.495,0,0,1,5.055,0,6.492,6.492,0,0,1,3.454,3.454,6.495,6.495,0,0,1,0,5.055,6.665,6.665,0,0,1-1.39,2.072,6.5,6.5,0,0,1-2.064,1.4A6.331,6.331,0,0,1,10.5,17Zm0-.975a5.318,5.318,0,0,0,3.917-1.617A5.339,5.339,0,0,0,16.029,10.5,5.495,5.495,0,0,0,10.5,4.975,5.339,5.339,0,0,0,6.593,6.585,5.318,5.318,0,0,0,4.975,10.5a5.326,5.326,0,0,0,1.617,3.909A5.326,5.326,0,0,0,10.5,16.029ZM10.5,10.5Z" transform="translate(-4 -4)"></path></svg></div></button></div></div></div><div class="problems_menu_wrap_content__BwiWt"><div class="right menu"><div class="problems_header_icons__h94Bp null"><svg xmlns="http://www.w3.org/2000/svg" width="23.092" height="23.092" viewBox="0 0 23.092 23.092"><g id="Group_13528" data-name="Group 13528" transform="translate(0.75 0.75)"><rect id="Rectangle_4008" data-name="Rectangle 4008" width="16" height="16" rx="2" transform="translate(5.592 5.592)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></rect><path id="Path_16033" data-name="Path 16033" d="M19.888,9.3V6.648A2.648,2.648,0,0,0,17.24,4H6.648A2.648,2.648,0,0,0,4,6.648V17.24a2.648,2.648,0,0,0,2.648,2.648H9.3" transform="translate(-4 -4)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></g></svg></div><div class="problems_header_icons__h94Bp null"><svg width="13" height="13" viewBox="0 0 13 13" fill="none" class="last_submit_code" xmlns="http://www.w3.org/2000/svg"><path d="M6.23954 8.39678C6.39839 8.55542 6.3984 8.81258 6.23956 8.97122C6.16013 9.05064 6.05634 9.09025 5.95234 9.09025C5.84834 9.09025 5.74454 9.05064 5.66512 8.97122L3.2656 6.50833L5.66512 4.04523C5.82376 3.88659 6.08092 3.88659 6.23956 4.04523C6.3984 4.20388 6.3984 4.46103 6.23956 4.61967L4.77015 6.08928H12.5959C12.8204 6.08928 13.0022 6.27128 13.0022 6.49553C13.0022 6.71978 12.8204 6.90178 12.5959 6.90178H4.74456L6.23954 8.39678ZM0.810635 0H8.12313C8.57204 0 8.93585 0.363797 8.93585 0.8125V4.46875H8.11787V1.30792C8.11787 1.03655 7.89768 0.816359 7.6263 0.816359H1.32049C1.04871 0.816359 0.828928 1.03655 0.828928 1.30792L0.816145 11.6963C0.816145 11.9677 1.03591 12.1879 1.30771 12.1879H7.6261C7.89748 12.1879 8.11766 11.9677 8.11766 11.6963V8.51784L8.93565 8.51886V12.1875C8.93565 12.6362 8.57185 13 8.12293 13H0.810431C0.361729 13 -0.00206947 12.6362 -0.00206947 12.1875V0.8125C-0.00186634 0.363797 0.361932 0 0.810635 0Z" fill="#fff"></path></svg></div><div class="problems_header_icons__h94Bp problems_editor_settings_icon__OqjCY"><svg xmlns="http://www.w3.org/2000/svg" width="25.5" height="25.5" viewBox="0 0 25.5 25.5"><g id="Group_13527" data-name="Group 13527" transform="translate(0.75 0.75)"><path id="Path_16032" data-name="Path 16032" d="M12.767,4.756a2.3,2.3,0,0,1,4.467,0,2.3,2.3,0,0,0,3.431,1.421,2.3,2.3,0,0,1,3.16,3.16,2.3,2.3,0,0,0,1.42,3.429,2.3,2.3,0,0,1,0,4.467,2.3,2.3,0,0,0-1.421,3.431,2.3,2.3,0,0,1-3.16,3.16,2.3,2.3,0,0,0-3.429,1.42,2.3,2.3,0,0,1-4.467,0,2.3,2.3,0,0,0-3.431-1.421,2.3,2.3,0,0,1-3.16-3.16,2.3,2.3,0,0,0-1.42-3.429,2.3,2.3,0,0,1,0-4.467A2.3,2.3,0,0,0,6.177,9.336a2.3,2.3,0,0,1,3.16-3.16,2.3,2.3,0,0,0,3.429-1.42Z" transform="translate(-3 -3)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><circle id="Ellipse_445" data-name="Ellipse 445" cx="4" cy="4" r="4" transform="translate(7.976 8)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></circle></g></svg></div><div class="problems_header_icons__h94Bp null"><svg id="noun-reset-3324862" xmlns="http://www.w3.org/2000/svg" width="24.627" height="23.999" viewBox="0 0 24.627 23.999"><path id="Path_16031" data-name="Path 16031" d="M164.4,74.27a.745.745,0,0,1-.74.65h-.1l-2.325-.3a12,12,0,1,1-9.45-4.62.75.75,0,0,1,0,1.5,10.5,10.5,0,1,0,8.15,3.885l-.125,2.9a.75.75,0,0,1-.745.715h-.035a.74.74,0,0,1-.715-.78l.2-4.655h0a.077.077,0,0,1,0-.035.38.38,0,0,1,0-.075v-.1a.075.075,0,0,1,0-.03.786.786,0,0,1,.045-.09.676.676,0,0,1,.07-.095.721.721,0,0,1,.155-.135.709.709,0,0,1,.1-.06l.1-.035h.295l4.395.585h0a.75.75,0,0,1,.72.785Z" transform="translate(-139.778 -69.995)" fill="#fff"></path></svg></div><div class="problems_header_icons__h94Bp null"><svg id="Group_13529" data-name="Group 13529" xmlns="http://www.w3.org/2000/svg" width="29.906" height="29.906" viewBox="0 0 29.906 29.906" class="maximize_height"><path id="Path_16034" data-name="Path 16034" d="M0,0H29.906V29.906H0Z" fill="none" class="outer_path"></path><path id="Path_16035" data-name="Path 16035" d="M16,4h4.984V8.984" transform="translate(3.938 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_430" data-name="Line 430" y1="7" x2="7" transform="translate(17.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16036" data-name="Path 16036" d="M8.984,20.984H4V16" transform="translate(0.984 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_431" data-name="Line 431" y1="8" x2="8" transform="translate(4.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16037" data-name="Path 16037" d="M16,20.984h4.984V16" transform="translate(3.938 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_432" data-name="Line 432" x2="7" y2="8" transform="translate(17.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16038" data-name="Path 16038" d="M8.984,4H4V8.984" transform="translate(0.984 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_433" data-name="Line 433" x2="8" y2="7" transform="translate(4.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line></svg></div></div></div></div></div><div class="pushable" style="overflow: hidden;"><div class="ui segment ui overlay top sidebar problems_editor_settings__RJyp_"><div class="ui center aligned two column grid problems_editor_settings__grid__kqdTl"><div class="three wide column problems_left__qRNlL"><h3>Editor Settings</h3><div class="problems_left_items__sTjhY"><p class="problems_active__IIP_r">Font Size</p><p class="">Theme</p></div></div><div class="thirteen wide column problems_right__yO8Lv"><p class="g-pt-1">Choose Your Preferred font For The Code Editor</p><div class="problems_right_options__r7n5j"><span class="">12px</span><span class="">13px</span><span class="problems_active__IIP_r">14px</span><span class="">15px</span><span class="">16px</span><span class="">18px</span><span class="">20px</span><span class="">22px</span></div></div></div></div><div class="pusher"><div id="editor" class="problems_editor_content__zXHUI"><div id="ace-editor" class=" ace_editor ace-tm" style="width: 100%; height: 100%; font-size: 14px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 144px; left: 215px;"></textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 49px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 49px;"><div class="ace_gutter-cell " style="height: 16px; top: 0px;">1<span class="ace_fold-widget ace_start ace_open" style="display: inline-block; height: 16px;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 16px;">2<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 32px;">3<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 48px;">4<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 64px;">5<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 80px;">6<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 96px;">7<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 112px;">8<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-active-line ace_gutter-cell " style="height: 16px; top: 128px;">9<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 144px;">10<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 160px;">11<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 176px;">12<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 192px;">13<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 208px;">14<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 224px;">15<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 240px;">16<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 256px;">17<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 272px;">18<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 288px;">19<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 304px;">20<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 320px;">21<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 336px;">22<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 352px;">23<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 368px;">24<span class="ace_fold-widget ace_start ace_open" style="height: 16px; display: inline-block;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 384px;">25<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 400px;">26<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 16px; top: 416px;">27<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 16px; left: 49px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 718px; height: 593px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 620px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 16px; top: 128px; left: 0px; right: 0px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line" style="height: 16px; top: 0px;"><span class="ace_keyword">class</span> <span class="ace_identifier">Solution</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 16px;">    </div><div class="ace_line" style="height: 16px; top: 32px;">    <span class="ace_comment">#Function to find minimum number of pages.</span></div><div class="ace_line" style="height: 16px; top: 48px;">    <span class="ace_keyword">def</span> <span class="ace_identifier">findPages</span><span class="ace_paren ace_lparen">(</span><span class="ace_variable ace_language">self</span><span class="ace_punctuation">,</span> <span class="ace_identifier">arr</span><span class="ace_punctuation">,</span> <span class="ace_identifier">m</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 64px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">def</span> <span class="ace_identifier">canweallocate</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">maxpages</span><span class="ace_punctuation">,</span> <span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 80px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">no_of_pages_allocated</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">arr</span><span class="ace_paren ace_lparen">[</span><span class="ace_constant ace_numeric">0</span><span class="ace_paren ace_rparen">]</span></div><div class="ace_line" style="height: 16px; top: 96px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">student</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 16px; top: 112px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">for</span> <span class="ace_identifier">pages</span> <span class="ace_keyword">in</span> <span class="ace_support ace_function">range</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">1</span><span class="ace_punctuation">,</span> <span class="ace_support ace_function">len</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">))</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 128px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span> <span class="ace_paren ace_lparen">(</span><span class="ace_identifier">arr</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">pages</span><span class="ace_paren ace_rparen">]</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_identifier">no_of_pages_allocated</span> <span class="ace_keyword ace_operator">&lt;=</span> <span class="ace_identifier">maxpages</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 144px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">no_of_pages_allocated</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_identifier">arr</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">pages</span><span class="ace_paren ace_rparen">]</span></div><div class="ace_line" style="height: 16px; top: 160px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">else</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 176px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">no_of_pages_allocated</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">arr</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">pages</span><span class="ace_paren ace_rparen">]</span></div><div class="ace_line" style="height: 16px; top: 192px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">student</span> <span class="ace_keyword ace_operator">+=</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 16px; top: 208px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">student</span></div><div class="ace_line" style="height: 16px; top: 224px;"></div><div class="ace_line" style="height: 16px; top: 240px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span> <span class="ace_identifier">m</span> <span class="ace_keyword ace_operator">&gt;</span> <span class="ace_support ace_function">len</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 256px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_keyword ace_operator">-</span><span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 16px; top: 272px;"><span class="ace_indent-guide">    </span>    <span class="ace_identifier">low</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_support ace_function">max</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">)</span></div><div class="ace_line" style="height: 16px; top: 288px;"><span class="ace_indent-guide">    </span>    <span class="ace_identifier">high</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_support ace_function">sum</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">)</span></div><div class="ace_line" style="height: 16px; top: 304px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">while</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">low</span> <span class="ace_keyword ace_operator">&lt;=</span> <span class="ace_identifier">high</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 320px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">maxpages</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_paren ace_lparen">(</span><span class="ace_identifier">low</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_identifier">high</span><span class="ace_paren ace_rparen">)</span> <span class="ace_keyword ace_operator">//</span> <span class="ace_constant ace_numeric">2</span></div><div class="ace_line" style="height: 16px; top: 336px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">if</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">canweallocate</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">maxpages</span><span class="ace_punctuation">,</span> <span class="ace_identifier">arr</span><span class="ace_paren ace_rparen">)</span> <span class="ace_keyword ace_operator">&lt;=</span> <span class="ace_identifier">m</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 352px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">high</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">maxpages</span> <span class="ace_keyword ace_operator">-</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 16px; top: 368px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_keyword">else</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 16px; top: 384px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">low</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">maxpages</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_constant ace_numeric">1</span></div><div class="ace_line" style="height: 16px; top: 400px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">low</span></div><div class="ace_line" style="height: 16px; top: 416px;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 128px; left: 166px; width: 8px; height: 16px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 11px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 11px; height: 432px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 11px; left: 49px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 11px; width: 718px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-optical-sizing: inherit; font-size-adjust: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></div></div><div class="ui segment ui overlay bottom sidebar problems_output_window__G_LTH  problems_normal_height__Og1iy"><div class="problems_header__E09Dq"><h4>Output Window</h4><div class="problems_header_icons__h94Bp"><div class="problems_header_icon__4Wp8F"><svg xmlns="http://www.w3.org/2000/svg" width="18.2" height="1.2" viewBox="0 0 18.2 1.2"><line id="Line_419" data-name="Line 419" x2="17" transform="translate(0.6 0.6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-width="1.2"></line></svg></div><div class="problems_header_icon__4Wp8F"><svg id="Group_13529" data-name="Group 13529" xmlns="http://www.w3.org/2000/svg" width="29.906" height="29.906" viewBox="0 0 29.906 29.906" class="maximize_height"><path id="Path_16034" data-name="Path 16034" d="M0,0H29.906V29.906H0Z" fill="none" class="outer_path"></path><path id="Path_16035" data-name="Path 16035" d="M16,4h4.984V8.984" transform="translate(3.938 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_430" data-name="Line 430" y1="7" x2="7" transform="translate(17.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16036" data-name="Path 16036" d="M8.984,20.984H4V16" transform="translate(0.984 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_431" data-name="Line 431" y1="8" x2="8" transform="translate(4.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16037" data-name="Path 16037" d="M16,20.984h4.984V16" transform="translate(3.938 3.938)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_432" data-name="Line 432" x2="7" y2="8" transform="translate(17.906 17)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path id="Path_16038" data-name="Path 16038" d="M8.984,4H4V8.984" transform="translate(0.984 0.984)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line id="Line_433" data-name="Line 433" x2="8" y2="7" transform="translate(4.906 5)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line></svg></div><div class="problems_header_icon__4Wp8F"><svg id="Group_8364" data-name="Group 8364" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path id="Path_7108" data-name="Path 7108" d="M0,0H24V24H0Z" fill="none" class="outer_path"></path><line id="Line_398" data-name="Line 398" x1="12" y2="12" transform="translate(6 6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"></line><line id="Line_399" data-name="Line 399" x2="12" y2="12" transform="translate(6 6)" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"></line></svg></div></div></div><div class="problems_content__I8YGa "><div class="ui green pointing secondary menu"><a class="item">Compilation Results</a><a class="item">Custom Input</a></div></div></div></div><div class="problems_footer__uv1_E" id="rightFooter"><div><div class="problems_hint_button__lcpQP"><span style="box-sizing: border-box; display: block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative;"><span style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 100% 0px 0px;"></span><img src="./Allocate Minimum Pages _ op_files/light-bulb(1)-1655185524.png" decoding="async" data-nimg="responsive" sizes="100vw" srcset="/_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=640&amp;q=75 640w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=750&amp;q=75 750w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=828&amp;q=75 828w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fimg-practice%2Flight-bulb(1)-1655185524.png&amp;w=3840&amp;q=75 3840w" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%;"></span></div></div><div><strong class="problems_custom_input__ediyL">Custom Input</strong><button class="ui mini button problems_compile_button__Lfluz">Compile &amp; Run</button><button class="ui button problems_submit_button__6QoNQ">Submit</button></div></div><div class="problems_bottom_report_issue__oEbhU"><div class="reportIssueModal_report_issue_button__KoQ6r"><button class="ui yellow mini button"><i aria-hidden="true" class="bug icon"></i>Report An Issue</button><span>If you are facing any issue on this page. Please let us know.</span></div></div></div></div></div></div></div></div></div></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"headerData":[{"title":"Courses","children":[{"title":"DSA to Development","children":[],"link":"https://www.geeksforgeeks.org/courses/dsa-to-development-coding-guide/"},{"title":"GATE 2026 Prep","children":[],"link":"https://www.geeksforgeeks.org/courses/category/gate/"},{"title":"Get 3 IBM Certifications","children":[],"link":"https://www.geeksforgeeks.org/courses/category/ibm-certification/"},{"title":"For Working Professionals","children":[{"title":"Interview 101: DSA \u0026 System Design","children":[],"link":"https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design"},{"title":"Data Science Training Program","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-applied-data-science-program/"},{"title":"JAVA Backend Development (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/Java-backend-live/"},{"title":"Data Analytics Training","children":[],"link":"https://www.geeksforgeeks.org/courses/data-analytics-training-program-excel-sql-python-powerbi"},{"title":"DevOps Engineering (LIVE)","children":[],"link":"https://www.geeksforgeeks.org/courses/devops-live/"},{"title":"Data Structures \u0026 Algorithms in Python","children":[],"link":"https://www.geeksforgeeks.org/courses/Data-Structures-With-Python/"}],"link":""},{"title":"For Students","children":[{"title":"Placement Preparation with DSA","children":[],"link":"https://www.geeksforgeeks.org/courses/placement-prep-programming-data-structures-algorithm"},{"title":"Data Science (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/data-science-live/"},{"title":"Data Structure \u0026 Algorithm-Self Paced (C++/JAVA)","children":[],"link":"https://www.geeksforgeeks.org/courses/dsa-self-paced/"},{"title":"Master Competitive Programming","children":[],"link":"https://www.geeksforgeeks.org/courses/competitive-programming-cp/"},{"title":"Full Stack Development with React \u0026 Node JS (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-node/"}],"link":""},{"title":"Full Stack Development","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-node/"},{"title":"Data Science \u0026 ML Program","children":[],"link":"https://www.geeksforgeeks.org/courses/data-science-live/"},{"title":"All Courses","children":[],"link":"https://www.geeksforgeeks.org/courses"}],"link":"https://practice.geeksforgeeks.org/courses/?ref=ghm"},{"title":"Tutorials","children":[{"title":"Data Structures \u0026 Algorithms","children":[],"link":"https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/"},{"title":"ML \u0026 Data Science","children":[],"link":"https://www.geeksforgeeks.org/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/"},{"title":"Interview Corner","children":[],"link":"https://www.geeksforgeeks.org/interview-corner/"},{"title":"Programming Languages","children":[],"link":"https://www.geeksforgeeks.org/programming-language-tutorials/"},{"title":"Web Development","children":[],"link":"https://www.geeksforgeeks.org/web-technology/"},{"title":"GATE","children":[],"link":"https://www.geeksforgeeks.org/gate-exam-tutorial/"},{"title":"CS Subjects","children":[],"link":"https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/"},{"title":"DevOps And Linux","children":[],"link":"https://www.geeksforgeeks.org/devops-and-linux-tutorial/"},{"title":"School Learning","children":[],"link":"https://www.geeksforgeeks.org/geeksforgeeks-school/"}],"link":""},{"title":"Practice","children":[{"title":"Practice Coding Problems","children":[],"link":"https://www.geeksforgeeks.org/geeksforgeeks-practice-best-online-coding-platform/"},{"title":"GfG 160: Summer Workshops","children":[],"link":"https://www.geeksforgeeks.org/courses/gfg-160-series"},{"title":"Problem of the Day","children":[],"link":"https://www.geeksforgeeks.org/problem-of-the-day"},{"title":"All Contests and Events","children":[],"link":"https://practice.geeksforgeeks.org/events"}],"link":""},{"title":"Jobs","children":[{"title":"Job-A-Thon Hiring Challenge","children":[],"link":"https://practice.geeksforgeeks.org/events/rec/job-a-thon"},{"title":"Get Hired","children":[],"link":"https://www.geeksforgeeks.org/jobs"},{"title":"Hire with us","children":[],"link":"https://www.geeksforgeeks.org/gfg-hiring-solutions-for-recruiters/"}],"link":"https://www.geeksforgeeks.org/jobs?utm_source=gfg\u0026utm_medium=gfg_header\u0026utm_campaign=gfgcontest_header"}],"canonicalUrlWithQueryParams":"https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1","canonicalUrlWithOutQueryParams":"https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1","cdnCountryCode":"IN","lightWeightHeader":false,"showNotificationHeader":true,"showTranslateHeader":true,"showSearchHeader":true,"isProblemPreview":false,"modifiedCanonical":"https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1","initialState":{"user":{"userVal":"","userError":false,"responsemsg":"","responsetype":"error","recaptchaError":false,"recaptchaValue":"","loading":false,"recpatchSiteKey":"6LexF0sUAAAAADiQjz9BMiSrqplrItl-tWYDSfWa","userData":null,"rememberMe":true,"theme":"light","gfgLogo":"https://media.geeksforgeeks.org/gfg-gg-logo.svg"},"myCoursesApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"myCoursesApi"}},"usersApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"usersApi"}},"jobsApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"jobsApi"}},"eventsApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"eventsApi"}},"listingPageApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"listingPageApi"}},"explorePageApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"explorePageApi"}},"coursesDashboardAPI":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"coursesDashboardAPI"}},"contestApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"contestApi"}},"registrationCntApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"registrationCntApi"}},"recurringEventApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"recurringEventApi"}},"problemApi":{"queries":{"getProblemDetails({\"isProblemPublic\":true,\"probResource\":\"allocate-minimum-number-of-pages0937\",\"problemBatchSlug\":null,\"problemTrackSlug\":null})":{"status":"fulfilled","endpointName":"getProblemDetails","requestId":"Ny5GTqivgMI48h6egUBnu","originalArgs":{"probResource":"allocate-minimum-number-of-pages0937","isProblemPublic":true,"problemBatchSlug":null,"problemTrackSlug":null},"startedTimeStamp":1748081079786,"data":{"id":701723,"problem_name":"Allocate Minimum Pages","problem_type":1,"problem_type_text":"Function","publish":1,"publish_date":"2019-12-30 13:09:37","slug":"allocate-minimum-number-of-pages0937","problem_level":1,"problem_level_text":"Medium","difficulty":"Medium","marks":4,"is_sample_input_modified":1,"custom_input_format":null,"multiple_testcase":1,"content_type":1,"visibility_type":1,"visibility_text":"public","is_contest_problem":0,"contest_slug":null,"can_add_interview_link":false,"can_edit_all_submissions_link":true,"has_all_submissions_button":false,"all_submissions":272092,"accuracy":"35.51%","is_user_login":0,"is_private_tag_visible":false,"related_courses":{},"tags":{"company_tags":["Infosys","Amazon","Microsoft","Google","Codenation","Uber"],"topic_tags":["Searching","Divide and Conquer","Algorithms"]},"problem_question":"\u003cp\u003e\u003cspan style=\"font-size: 14pt;\"\u003eYou are given an array \u003ccode\u003earr[]\u003c/code\u003e of integers, where each element \u003ccode\u003earr[i]\u003c/code\u003e represents the number of pages in the ith book. You also have an integer \u003ccode\u003ek\u003c/code\u003e representing the number of students. The task is to allocate books to each student such that:\u003c/span\u003e\u003c/p\u003e\n\u003cul\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eEach student receives \u003cstrong\u003eatleast\u003c/strong\u003e one book.\u003c/span\u003e\u003c/li\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eEach student is assigned a contiguous sequence of books.\u003c/span\u003e\u003c/li\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eNo book is assigned to more than one student.\u003c/span\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 14pt;\"\u003eThe objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.\u003c/span\u003e\u003c/p\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eNote\u003c/strong\u003e: Return \u003cstrong\u003e-1\u003c/strong\u003e if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).\u003c/span\u003e\u003c/p\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eExamples:\u003c/strong\u003e\u003c/span\u003e\u003c/p\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [12, 34, 67, 90], k = 2\n\u003cstrong\u003eOutput: \u003c/strong\u003e113\n\u003cstrong\u003eExplanation: \u003c/strong\u003eAllocation can be done in following ways:\n[12] and [34, 67, 90] Maximum Pages = 191\n[12, 34] and [67, 90] Maximum Pages = 157\n[12, 34, 67] and [90] Maximum Pages = 113.\nTherefore, the minimum of these cases is 113, which is selected as the output.\u003c/span\u003e\u003c/pre\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [15, 17, 20], k = 5\n\u003cstrong\u003eOutput: \u003c/strong\u003e-1\n\u003cstrong\u003eExplanation: \u003c/strong\u003eAllocation can not be done.\u003cbr /\u003e\u003c/span\u003e\u003c/pre\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 14pt;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [22, 23, 67], k = 1\n\u003cstrong\u003eOutput: \u003c/strong\u003e112\u003c/span\u003e\u003c/pre\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eConstraints:\u003c/strong\u003e\u003cbr /\u003e1 \u0026lt;=\u0026nbsp; arr.size() \u0026lt;= 10\u003csup\u003e6\u003c/sup\u003e\u003cbr /\u003e1 \u0026lt;= arr[i] \u0026lt;= 10\u003csup\u003e3\u003cbr /\u003e\u003c/sup\u003e\u003c/span\u003e\u003cspan style=\"font-size: 18px;\"\u003e1 \u0026lt;= k \u0026lt;= 10\u003csup\u003e3\u0026nbsp;\u003c/sup\u003e\u003c/span\u003e\u003c/p\u003e","contributor":"Shivam Gupta","test_cases":"12 34 67 90\u0026!//!\u00262","article_existence":1,"article_list":["https://www.geeksforgeeks.org/allocate-minimum-number-pages/"],"can_edit_history":false,"can_edit_problem":false,"can_edit_problem_read_only":false,"author":"madhuradlakha","has_problem_solutions":true,"has_hints":true,"has_editorial":true,"can_view_hints":true,"track":"","batch":"","has_doubt_assistance":false,"extra":{},"course_default_lang":null,"interview_links":["https://www.geeksforgeeks.org/amazon-interview-experience-on-campus-for-sde-1-5/"],"user_has_access_to_doubt_assistance":false,"editorial_type":"post","associated_func_pid":null,"can_view_author_solution":false,"show_editorial_tab":true,"is_todays_potd":false,"visualizer_type":null,"input_format":{"arguments":"arr[] =\u0026!//!\u0026k = ","datatype":"INTEGER_ARRAY\u0026!//!\u0026INTEGER"}},"fulfilledTimeStamp":1748081079796}},"mutations":{},"provided":{},"subscriptions":{"getProblemDetails({\"isProblemPublic\":true,\"probResource\":\"allocate-minimum-number-of-pages0937\",\"problemBatchSlug\":null,\"problemTrackSlug\":null})":{"Ny5GTqivgMI48h6egUBnu":{}}},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"problemApi"}},"batchApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"batchApi"}},"trackApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"trackApi"}},"ideApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"ideApi"}},"generalApi":{"queries":{"getAuthHeaderData({\"params\":null})":{"status":"fulfilled","endpointName":"getAuthHeaderData","requestId":"Ms7btAg5uYrB4Trvfogh_","originalArgs":{"params":null},"startedTimeStamp":1748081079772,"data":[{"title":"Courses","children":[{"title":"DSA to Development","children":[],"link":"https://www.geeksforgeeks.org/courses/dsa-to-development-coding-guide/"},{"title":"GATE 2026 Prep","children":[],"link":"https://www.geeksforgeeks.org/courses/category/gate/"},{"title":"Get 3 IBM Certifications","children":[],"link":"https://www.geeksforgeeks.org/courses/category/ibm-certification/"},{"title":"For Working Professionals","children":[{"title":"Interview 101: DSA \u0026 System Design","children":[],"link":"https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design"},{"title":"Data Science Training Program","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-applied-data-science-program/"},{"title":"JAVA Backend Development (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/Java-backend-live/"},{"title":"Data Analytics Training","children":[],"link":"https://www.geeksforgeeks.org/courses/data-analytics-training-program-excel-sql-python-powerbi"},{"title":"DevOps Engineering (LIVE)","children":[],"link":"https://www.geeksforgeeks.org/courses/devops-live/"},{"title":"Data Structures \u0026 Algorithms in Python","children":[],"link":"https://www.geeksforgeeks.org/courses/Data-Structures-With-Python/"}],"link":""},{"title":"For Students","children":[{"title":"Placement Preparation with DSA","children":[],"link":"https://www.geeksforgeeks.org/courses/placement-prep-programming-data-structures-algorithm"},{"title":"Data Science (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/data-science-live/"},{"title":"Data Structure \u0026 Algorithm-Self Paced (C++/JAVA)","children":[],"link":"https://www.geeksforgeeks.org/courses/dsa-self-paced/"},{"title":"Master Competitive Programming","children":[],"link":"https://www.geeksforgeeks.org/courses/competitive-programming-cp/"},{"title":"Full Stack Development with React \u0026 Node JS (Live)","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-node/"}],"link":""},{"title":"Full Stack Development","children":[],"link":"https://www.geeksforgeeks.org/courses/full-stack-node/"},{"title":"Data Science \u0026 ML Program","children":[],"link":"https://www.geeksforgeeks.org/courses/data-science-live/"},{"title":"All Courses","children":[],"link":"https://www.geeksforgeeks.org/courses"}],"link":"https://practice.geeksforgeeks.org/courses/?ref=ghm"},{"title":"Tutorials","children":[{"title":"Data Structures \u0026 Algorithms","children":[],"link":"https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/"},{"title":"ML \u0026 Data Science","children":[],"link":"https://www.geeksforgeeks.org/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/"},{"title":"Interview Corner","children":[],"link":"https://www.geeksforgeeks.org/interview-corner/"},{"title":"Programming Languages","children":[],"link":"https://www.geeksforgeeks.org/programming-language-tutorials/"},{"title":"Web Development","children":[],"link":"https://www.geeksforgeeks.org/web-technology/"},{"title":"GATE","children":[],"link":"https://www.geeksforgeeks.org/gate-exam-tutorial/"},{"title":"CS Subjects","children":[],"link":"https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/"},{"title":"DevOps And Linux","children":[],"link":"https://www.geeksforgeeks.org/devops-and-linux-tutorial/"},{"title":"School Learning","children":[],"link":"https://www.geeksforgeeks.org/geeksforgeeks-school/"}],"link":""},{"title":"Practice","children":[{"title":"Practice Coding Problems","children":[],"link":"https://www.geeksforgeeks.org/geeksforgeeks-practice-best-online-coding-platform/"},{"title":"GfG 160: Summer Workshops","children":[],"link":"https://www.geeksforgeeks.org/courses/gfg-160-series"},{"title":"Problem of the Day","children":[],"link":"https://www.geeksforgeeks.org/problem-of-the-day"},{"title":"All Contests and Events","children":[],"link":"https://practice.geeksforgeeks.org/events"}],"link":""},{"title":"Jobs","children":[{"title":"Job-A-Thon Hiring Challenge","children":[],"link":"https://practice.geeksforgeeks.org/events/rec/job-a-thon"},{"title":"Get Hired","children":[],"link":"https://www.geeksforgeeks.org/jobs"},{"title":"Hire with us","children":[],"link":"https://www.geeksforgeeks.org/gfg-hiring-solutions-for-recruiters/"}],"link":"https://www.geeksforgeeks.org/jobs?utm_source=gfg\u0026utm_medium=gfg_header\u0026utm_campaign=gfgcontest_header"}],"fulfilledTimeStamp":1748081079784},"getPromotionalEventsApi({\"cdnCountryCode\":\"IN\",\"pageSource\":\"problems\"})":{"status":"fulfilled","endpointName":"getPromotionalEventsApi","requestId":"V6DgafBIkIuN8K2IYWqaf","originalArgs":{"pageSource":"problems","cdnCountryCode":"IN"},"startedTimeStamp":1748081079798,"data":{"upcoming_events":{"compilation_results_banner":[{"promotional_banner_id":88,"page_source":2,"page_element":"compilation_results_banner","display_order":1,"title":"\u003cp\u003eKick start your career with GfG 160!\u003cbr data-mce-bogus=\"1\"\u003e\u003c/p\u003e","description":"\u003cp\u003e\u003cbr data-mce-bogus=\"1\"\u003e\u003c/p\u003e","short_description":"\u003cp\u003e\u003cbr data-mce-bogus=\"1\"\u003e\u003c/p\u003e","button_text":"\u003cp\u003e\u003cbr data-mce-bogus=\"1\"\u003e\u003c/p\u003e","click_id":"","icon_url":null,"dark_mode_icon_url":null,"redirect_url":"https://www.geeksforgeeks.org/courses/gfg-160-series","background_color":"","dark_mode_background_color":"","button_background_color":null,"is_default":1,"start_date":null,"end_date":null,"country":0}]}},"fulfilledTimeStamp":1748081079811}},"mutations":{},"provided":{},"subscriptions":{"getAuthHeaderData({\"params\":null})":{"Ms7btAg5uYrB4Trvfogh_":{}},"getPromotionalEventsApi({\"cdnCountryCode\":\"IN\",\"pageSource\":\"problems\"})":{"V6DgafBIkIuN8K2IYWqaf":{}}},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"generalApi"}},"allFeedbacksApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"allFeedbacksApi"}},"dashboardBaseApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"dashboardBaseApi"}},"addEditCourseFeaturesApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"addEditCourseFeaturesApi"}},"filtersApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"filtersApi"}},"paymentTransactionHistoryApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"paymentTransactionHistoryApi"}},"classAllApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"classAllApi"}},"sidebarApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"sidebarApi"}},"addEditJobsApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"addEditJobsApi"}},"addEditProblemApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"addEditProblemApi"}},"hackathonApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"hackathonApi"}},"hackathonNewApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"hackathonNewApi"}},"problemData":{"isProblemPublic":true,"problemUserScore":0,"problemAttempted":{"solvedProblemId":null,"status":-1},"problemUserScoreUpdated":false,"probResource":"allocate-minimum-number-of-pages0937","problemBatchSlug":null,"problemTrackSlug":null,"hasViewedSubmission":false,"allData":{"probData":{"id":701723,"problem_name":"Allocate Minimum Pages","problem_type":1,"problem_type_text":"Function","publish":1,"publish_date":"2019-12-30 13:09:37","slug":"allocate-minimum-number-of-pages0937","problem_level":1,"problem_level_text":"Medium","difficulty":"Medium","marks":4,"is_sample_input_modified":1,"custom_input_format":null,"multiple_testcase":1,"content_type":1,"visibility_type":1,"visibility_text":"public","is_contest_problem":0,"contest_slug":null,"can_add_interview_link":false,"can_edit_all_submissions_link":true,"has_all_submissions_button":false,"all_submissions":272092,"accuracy":"35.51%","is_user_login":0,"is_private_tag_visible":false,"related_courses":{},"tags":{"company_tags":["Infosys","Amazon","Microsoft","Google","Codenation","Uber"],"topic_tags":["Searching","Divide and Conquer","Algorithms"]},"problem_question":"\u003cp\u003e\u003cspan style=\"font-size: 14pt;\"\u003eYou are given an array \u003ccode\u003earr[]\u003c/code\u003e of integers, where each element \u003ccode\u003earr[i]\u003c/code\u003e represents the number of pages in the ith book. You also have an integer \u003ccode\u003ek\u003c/code\u003e representing the number of students. The task is to allocate books to each student such that:\u003c/span\u003e\u003c/p\u003e\n\u003cul\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eEach student receives \u003cstrong\u003eatleast\u003c/strong\u003e one book.\u003c/span\u003e\u003c/li\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eEach student is assigned a contiguous sequence of books.\u003c/span\u003e\u003c/li\u003e\n\u003cli\u003e\u003cspan style=\"font-size: 14pt;\"\u003eNo book is assigned to more than one student.\u003c/span\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 14pt;\"\u003eThe objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.\u003c/span\u003e\u003c/p\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eNote\u003c/strong\u003e: Return \u003cstrong\u003e-1\u003c/strong\u003e if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).\u003c/span\u003e\u003c/p\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eExamples:\u003c/strong\u003e\u003c/span\u003e\u003c/p\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [12, 34, 67, 90], k = 2\n\u003cstrong\u003eOutput: \u003c/strong\u003e113\n\u003cstrong\u003eExplanation: \u003c/strong\u003eAllocation can be done in following ways:\n[12] and [34, 67, 90] Maximum Pages = 191\n[12, 34] and [67, 90] Maximum Pages = 157\n[12, 34, 67] and [90] Maximum Pages = 113.\nTherefore, the minimum of these cases is 113, which is selected as the output.\u003c/span\u003e\u003c/pre\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [15, 17, 20], k = 5\n\u003cstrong\u003eOutput: \u003c/strong\u003e-1\n\u003cstrong\u003eExplanation: \u003c/strong\u003eAllocation can not be done.\u003cbr /\u003e\u003c/span\u003e\u003c/pre\u003e\n\u003cpre\u003e\u003cspan style=\"font-size: 14pt;\"\u003e\u003cstrong\u003eInput: \u003c/strong\u003earr[] = [22, 23, 67], k = 1\n\u003cstrong\u003eOutput: \u003c/strong\u003e112\u003c/span\u003e\u003c/pre\u003e\n\u003cp\u003e\u003cspan style=\"font-size: 18px;\"\u003e\u003cstrong\u003eConstraints:\u003c/strong\u003e\u003cbr /\u003e1 \u0026lt;=\u0026nbsp; arr.size() \u0026lt;= 10\u003csup\u003e6\u003c/sup\u003e\u003cbr /\u003e1 \u0026lt;= arr[i] \u0026lt;= 10\u003csup\u003e3\u003cbr /\u003e\u003c/sup\u003e\u003c/span\u003e\u003cspan style=\"font-size: 18px;\"\u003e1 \u0026lt;= k \u0026lt;= 10\u003csup\u003e3\u0026nbsp;\u003c/sup\u003e\u003c/span\u003e\u003c/p\u003e","contributor":"Shivam Gupta","test_cases":"12 34 67 90\u0026!//!\u00262","article_existence":1,"article_list":["https://www.geeksforgeeks.org/allocate-minimum-number-pages/"],"can_edit_history":false,"can_edit_problem":false,"can_edit_problem_read_only":false,"author":"madhuradlakha","has_problem_solutions":true,"has_hints":true,"has_editorial":true,"can_view_hints":true,"track":"","batch":"","has_doubt_assistance":false,"extra":{},"course_default_lang":null,"interview_links":["https://www.geeksforgeeks.org/amazon-interview-experience-on-campus-for-sde-1-5/"],"user_has_access_to_doubt_assistance":false,"editorial_type":"post","associated_func_pid":null,"can_view_author_solution":false,"show_editorial_tab":true,"is_todays_potd":false,"visualizer_type":null,"input_format":{"arguments":"arr[] =\u0026!//!\u0026k = ","datatype":"INTEGER_ARRAY\u0026!//!\u0026INTEGER"}},"metaData":{}},"isProblemDemo":false,"hasMovedToEditor":false,"nextProblemData":null,"nextProblemClickId":"","userEntityId":"","yogiBotPremiumTourType":null,"isMtcEnabled":false,"isSampleInputModified":false,"isSeparateInputAvailable":false},"allUserSprint":{"sprintData":[]},"generalData":{"tinyMceScriptLoaded":null},"batchTrackData":{"batchId":null,"trackId":null,"userBatchScore":0,"userBatchScoreUpdated":false,"userBatchProgress":-1,"userSubmittedProblemIds":[],"userTrackProgress":{},"userVideosData":{},"liveClassesVideosData":{},"courseSlug":"","courseFeeType":"","isBatchAccessPermissionApiExecuted":false,"userPaidAccess":false,"isBatchRated":null,"notesDetails":{"notes_list":[],"last_evaluated_key":null},"entityNotesIdDetails":{},"enableAddNotesButton":false,"isNotesModalOpen":false,"isBatchModerationOn":false},"rewardAPI":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"rewardAPI"}},"contestData":{"isContestEndedForUser":null,"isContestEnded":true,"fixedContestLiveButUserEnded":false,"someErrorOccured":false,"quizStatusCount":{},"problemsStatusCount":{},"showFinishTestModal":false,"disableCopyPaste":false,"isProctoredTerminated":false,"proctoredContest":false,"showFeedbackTestModal":false,"isAutoEnd":false,"showCalculator":false,"quiz":{"showQuizAnswers":false,"activeIndex":{"question":0,"section":0},"userResponses":null,"revealButtonText":"Reveal Answer","displayCorrectAnswer":false,"submitButtonText":null,"submissionsStatus":null},"problems":{"submissionType":"mySubmissions","submissions":null,"openedProblemId":null,"userCodingResponse":{}},"leaderboard":{"currentPage":1,"leaderboardType":"current"}},"couponData":{"activeTab":"General Settings","formValues":{"General Settings":{"coupon_code":"","coupon_id":"","valid_till":null,"valid_from":null,"usage_details":null,"coupon_type":null,"discount_details":{"up_to":-1},"coupon_desc":null,"coupon_college_domain":null},"Discount Rules":{"customer_rules":{},"purchase_rules":{},"product_rules":{}},"Assign Publish":{"created_type":null,"publish_status":null,"assignee_commission":null,"created_by_team":null,"assign_to":null,"assignee_type":null,"purpose_created":null},"Create Copies":{"copy_count":0},"Influencer details":{"user_name":"","email":"","contact_number":null,"onboarding":null,"subject":"","email_body":""}},"selectedEntities":{"entitled_cust":[],"entitled_prod":[],"prerequisite_prod":[]}},"problemOfTheDayAPI":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"problemOfTheDayAPI"}},"addEditCourseData":{"activeTab":"Course Intro","activeTabIndex":0,"formValues":{"courseIntro":{"course_name":"","course_short_name":"","course_slug":"","short_description":"","course_for_kids":0,"course_type":1,"listing_type":0,"course_fee_type":1,"auto_registration":0,"course_default_lang":null,"best_suited_for":"","default_testimonial":{"name":"","achievements":"","content":""},"course_publish_date":null,"expiry_date":null,"redirection_url":null,"has_doubt_assistance":0,"free_doubt_support_expiry_date":0,"doubt_support_expiry_date":6,"course_image_text":"","show_kapture_chat_box":0,"show_placement_assistance_banner":0,"doubt_assistance_price":0,"what_you_will_learn":"","course_email_content":"","intro_video_link":"","broucher_link":"","warning_message":"","show_mentor_rating":0,"level":null,"seats_left":null,"course_duration":null,"urgency_start_time":null,"urgency_end_time":null,"doubt_assistance_banner":0,"syllabus_pdf":0,"email_content_redirection_link":"","course_redirection_slug":"","payment_deep_link":"","course_expiry_days":365,"show_all_live_classes":false,"skills":[],"is_payment_qrcode_generated":0,"live_classes_batches":[],"has_scheduler":false,"scheduler_batches":[],"notes_batches":[],"show_notes_tab":false},"courseBanners":[{"title":"Old Thumbnail Banner","banner_type":"thumbnail-old","banner_key":"thumbnail_old","image_url":"thumbnail_old_image_url","exists":false,"file":null},{"title":"Facebook Banner","banner_type":"social","banner_key":"social","image_url":"social_image_url","exists":false,"file":null},{"title":"Mobile Banner","banner_type":"mobile","banner_key":"mobile","image_url":"mobile_image_url","exists":false,"file":null},{"title":"Thumbnail Banner","banner_type":"thumbnail","banner_key":"thumbnail","image_url":"thumbnail_image_url","exists":false,"file":null},{"title":"Payment Checkout Image","banner_type":"payment-checkout-image","banner_key":"payment_checkout_image","image_url":"payment_checkout_image_image_url","exists":false,"file":null},{"title":"Course Video Thumbnail Image","banner_type":"course-video-thumbnail-image","banner_key":"course_video_thumbnail_image","image_url":"course_video_thumbnail_image_image_url","exists":false,"file":null},{"title":"Course Overview Image","banner_type":"course-overview-image","banner_key":"course_overview_image","image_url":"course_overview_image_image_url","exists":false,"file":null},{"title":"What will you learn image","banner_type":"course-what-will-you-learn","banner_key":"course_what_will_you_learn","image_url":"course_what_will_you_learn_image_url","exists":false,"file":null}],"upgradableCourses":[],"electiveCourses":[],"courseBenefits":[],"courseContent":[],"faqs":[],"courseFaqs":[],"schemaKeywords":[],"emailContent":[],"optLanguages":[],"courseJourneyPhases":[]},"isEdit":false,"errorObj":null,"showConfirmationModal":false,"deleteContext":null},"jobPortalData":{"activeTab":"dashboard","jobDetails":{"organization":{"name":"","website":"","logo":"","about":""},"designation":{"text":"","id":""},"location_type":"","location":[],"employment_type":"","description":"","salary":{"min":"","max":"","salary_type":2},"experience":{"min":"","max":""},"last_apply_date":"","publish_date":"","skill_sets":[]},"activeModal":{"type":null,"data":{}},"productDetails":{},"hasSignedLegalContract":null},"jobPortalApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"jobPortalApi"}},"collegeAdminData":{"canAccessPage":null},"geekOlympics":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"geekOlympics"}},"summerTrainingEvent":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"summerTrainingEvent"}},"dsaToDevelopmentApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"dsaToDevelopmentApi"}},"dsaToDevelopmentData":{"hasRegistered":null,"currentQuestion":null,"hasCompletedSurvey":null,"hasAttemptedSurvey":null,"batchId":null,"applicationStatus":null,"submittedLastQuestion":false,"isIndianUser":null},"organizationDashboardApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"organizationDashboardApi"}},"organizationDashboardData":{"organizationName":null,"organizationSlug":null,"organizationType":null,"organizationId":null,"currentDate":null,"routeSpecificErrors":{"my-courses":null,"course-management":null,"student-repository":null,"aggregated-report":null},"pageError":null},"userInfo":{"userCountry":"IN","mobileDevice":false},"myCoursesData":{"is_user_organization_deal":false},"aggregatedReportData":{"page":1,"batches":null,"contests":null,"institutes":[],"degrees":[],"branches":[],"sections":[],"search":"","sortBy":"-avg_score","batchesOptions":[],"contestOptions":[],"batchContestOptionsMap":{},"institutesOptions":null,"degreesOptions":null,"instituteMapping":{},"sectionOptions":null,"branchOptions":null,"universityDetailsState":{"status":"idle","error":null},"clickedOnRedirection":false},"leaderboardApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"leaderboardApi"}},"premiumApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"premiumApi"}},"termsOfServiceApi":{"queries":{},"mutations":{},"provided":{},"subscriptions":{},"config":{"online":true,"focused":true,"middlewareRegistered":true,"refetchOnFocus":false,"refetchOnReconnect":false,"refetchOnMountOrArgChange":false,"keepUnusedDataFor":60,"reducerPath":"termsOfServiceApi"}}}},"__N_SSP":true},"page":"/problems/[probResource]/[probType]","query":{"probResource":"allocate-minimum-number-of-pages0937","probType":"1"},"buildId":"FgJJ5Mmgh7Al2Suq6JBEL","isFallback":false,"dynamicIds":[83819],"gssp":true,"scriptLoader":[]}</script><script src="./Allocate Minimum Pages _ op_files/tinymce.min.js.download" data-nscript="afterInteractive"></script><iframe allow="join-ad-interest-group" data-tagging-id="AW-796001856" data-load-time="1748081342818" height="0" width="0" src="./Allocate Minimum Pages _ op_files/796001856.html" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" style="display: none; visibility: hidden;" src="./Allocate Minimum Pages _ op_files/saved_resource(1).html"></iframe><next-route-announcer><p aria-live="assertive" id="__next-route-announcer__" role="alert" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; white-space: nowrap; overflow-wrap: normal;"></p></next-route-announcer>
      <script type="text/javascript" id="" charset="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","2320390688070878");fbq("track","PageView");</script>
      <noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=2320390688070878&amp;ev=PageView&amp;noscript=1"></noscript>
    <meta name="facebook-domain-verification" content="xcg0z3utjhf3w2e7wftoypcx8j3l5s">
<script type="text/javascript" id="" charset="">!function(d,e,f,a,b,c){d.twq||(a=d.twq=function(){a.exe?a.exe.apply(a,arguments):a.queue.push(arguments)},a.version="1.1",a.queue=[],b=e.createElement(f),b.async=!0,b.src="//static.ads-twitter.com/uwt.js",c=e.getElementsByTagName(f)[0],c.parentNode.insertBefore(b,c))}(window,document,"script");twq("init","o65zz");twq("track","PageView");</script><iframe allow="join-ad-interest-group" data-tagging-id="AW-796001856" data-load-time="1748081342987" height="0" width="0" src="./Allocate Minimum Pages _ op_files/796001856(1).html" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="AW-474915276" data-load-time="1748081343359" height="0" width="0" src="./Allocate Minimum Pages _ op_files/474915276.html" style="display: none; visibility: hidden;"></iframe>
<img src="./Allocate Minimum Pages _ op_files/adsct" height="1" width="1" style="display: none;"><img src="./Allocate Minimum Pages _ op_files/adsct(1)" height="1" width="1" style="display: none;"><div id="batBeacon97816876285" style="width: 0px; height: 0px; display: none; visibility: hidden;"><img id="batBeacon989142918585" width="0" height="0" alt="" src="./Allocate Minimum Pages _ op_files/0" style="width: 0px; height: 0px; display: none; visibility: hidden;"></div><div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; width: 0px; height: 0px;"><div></div></div></div><script src="./Allocate Minimum Pages _ op_files/tinymce.min.js.download" defer=""></script><div class="tox tox-silver-sink tox-tinymce-aux" style="position: relative;"></div></body></html>