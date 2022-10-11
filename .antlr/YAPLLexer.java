// Generated from /home/luis/Desktop/college/last-semester/compilers/proyecto-2-compiladores-v1/YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, CLASS=12, INHERITS=13, TRUE=14, FALSE=15, IF=16, ELSE=17, 
		THEN=18, FI=19, WHILE=20, LOOP=21, POOL=22, LET=23, IN=24, NEW=25, ISVOID=26, 
		ADD=27, MINUS=28, MULT=29, DIV=30, LT=31, LE=32, EQ=33, NOT=34, STRINGS=35, 
		INTEGERS=36, TYPE=37, ID=38, ASIGNOPP=39, ONE_LINE_COMMENT=40, MULTILINE_COMMENT=41, 
		WHITESPACE=42;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "CLASS", "INHERITS", "TRUE", "FALSE", "IF", "ELSE", 
			"THEN", "FI", "WHILE", "LOOP", "POOL", "LET", "IN", "NEW", "ISVOID", 
			"ADD", "MINUS", "MULT", "DIV", "LT", "LE", "EQ", "NOT", "STRINGS", "INTEGERS", 
			"TYPE", "ID", "ASIGNOPP", "ONE_LINE_COMMENT", "MULTILINE_COMMENT", "WHITESPACE", 
			"A", "C", "D", "E", "F", "H", "I", "L", "N", "O", "P", "R", "S", "T", 
			"U", "V", "W", "X", "Y", "Z", "HEX", "UNICODE", "ESC"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
			"'let'", "'~'", null, null, "'true'", "'false'", null, null, null, null, 
			null, null, null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", 
			"'<'", "'<='", "'='", null, null, null, null, null, "'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"CLASS", "INHERITS", "TRUE", "FALSE", "IF", "ELSE", "THEN", "FI", "WHILE", 
			"LOOP", "POOL", "LET", "IN", "NEW", "ISVOID", "ADD", "MINUS", "MULT", 
			"DIV", "LT", "LE", "EQ", "NOT", "STRINGS", "INTEGERS", "TYPE", "ID", 
			"ASIGNOPP", "ONE_LINE_COMMENT", "MULTILINE_COMMENT", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YAPLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u0174\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6"+
		"\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3"+
		"!\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\7$\u0100\n$\f$\16$\u0103\13$\3$\3$\3%\6"+
		"%\u0108\n%\r%\16%\u0109\3&\3&\7&\u010e\n&\f&\16&\u0111\13&\3\'\3\'\7\'"+
		"\u0115\n\'\f\'\16\'\u0118\13\'\3(\3(\3(\3)\3)\3)\3)\7)\u0121\n)\f)\16"+
		")\u0124\13)\3)\5)\u0127\n)\3)\3)\3*\3*\3*\3*\7*\u012f\n*\f*\16*\u0132"+
		"\13*\3*\3*\3*\3*\3*\3+\6+\u013a\n+\r+\16+\u013b\3+\3+\3,\3,\3-\3-\3.\3"+
		".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3"+
		"\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@"+
		"\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\5B\u0173\nB\3\u0130\2C\3\3\5\4\7\5\t\6"+
		"\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24"+
		"\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K"+
		"\'M(O)Q*S+U,W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2"+
		"}\2\177\2\u0081\2\u0083\2\3\2\37\4\2$$^^\3\2\62;\3\2C\\\6\2\62;C\\aac"+
		"|\3\2c|\3\2\f\f\5\2\13\f\16\17\"\"\4\2CCcc\4\2EEee\4\2FFff\4\2GGgg\4\2"+
		"HHhh\4\2JJjj\4\2KKkk\4\2NNnn\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4"+
		"\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\5\2\62;CHch\n"+
		"\2$$\61\61^^ddhhppttvv\2\u0166\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t"+
		"\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2"+
		"\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2"+
		"\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2"+
		"+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2"+
		"\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2"+
		"C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3"+
		"\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3\u0085\3\2\2\2\5\u0087\3\2\2"+
		"\2\7\u0089\3\2\2\2\t\u008b\3\2\2\2\13\u008d\3\2\2\2\r\u008f\3\2\2\2\17"+
		"\u0091\3\2\2\2\21\u0093\3\2\2\2\23\u0095\3\2\2\2\25\u0097\3\2\2\2\27\u009b"+
		"\3\2\2\2\31\u009d\3\2\2\2\33\u00a3\3\2\2\2\35\u00ac\3\2\2\2\37\u00b1\3"+
		"\2\2\2!\u00b7\3\2\2\2#\u00ba\3\2\2\2%\u00bf\3\2\2\2\'\u00c4\3\2\2\2)\u00c7"+
		"\3\2\2\2+\u00cd\3\2\2\2-\u00d2\3\2\2\2/\u00d7\3\2\2\2\61\u00db\3\2\2\2"+
		"\63\u00de\3\2\2\2\65\u00e2\3\2\2\2\67\u00e9\3\2\2\29\u00eb\3\2\2\2;\u00ed"+
		"\3\2\2\2=\u00ef\3\2\2\2?\u00f1\3\2\2\2A\u00f3\3\2\2\2C\u00f6\3\2\2\2E"+
		"\u00f8\3\2\2\2G\u00fc\3\2\2\2I\u0107\3\2\2\2K\u010b\3\2\2\2M\u0112\3\2"+
		"\2\2O\u0119\3\2\2\2Q\u011c\3\2\2\2S\u012a\3\2\2\2U\u0139\3\2\2\2W\u013f"+
		"\3\2\2\2Y\u0141\3\2\2\2[\u0143\3\2\2\2]\u0145\3\2\2\2_\u0147\3\2\2\2a"+
		"\u0149\3\2\2\2c\u014b\3\2\2\2e\u014d\3\2\2\2g\u014f\3\2\2\2i\u0151\3\2"+
		"\2\2k\u0153\3\2\2\2m\u0155\3\2\2\2o\u0157\3\2\2\2q\u0159\3\2\2\2s\u015b"+
		"\3\2\2\2u\u015d\3\2\2\2w\u015f\3\2\2\2y\u0161\3\2\2\2{\u0163\3\2\2\2}"+
		"\u0165\3\2\2\2\177\u0167\3\2\2\2\u0081\u0169\3\2\2\2\u0083\u016f\3\2\2"+
		"\2\u0085\u0086\7=\2\2\u0086\4\3\2\2\2\u0087\u0088\7}\2\2\u0088\6\3\2\2"+
		"\2\u0089\u008a\7\177\2\2\u008a\b\3\2\2\2\u008b\u008c\7*\2\2\u008c\n\3"+
		"\2\2\2\u008d\u008e\7.\2\2\u008e\f\3\2\2\2\u008f\u0090\7+\2\2\u0090\16"+
		"\3\2\2\2\u0091\u0092\7<\2\2\u0092\20\3\2\2\2\u0093\u0094\7B\2\2\u0094"+
		"\22\3\2\2\2\u0095\u0096\7\60\2\2\u0096\24\3\2\2\2\u0097\u0098\7n\2\2\u0098"+
		"\u0099\7g\2\2\u0099\u009a\7v\2\2\u009a\26\3\2\2\2\u009b\u009c\7\u0080"+
		"\2\2\u009c\30\3\2\2\2\u009d\u009e\5Y-\2\u009e\u009f\5e\63\2\u009f\u00a0"+
		"\5W,\2\u00a0\u00a1\5o8\2\u00a1\u00a2\5o8\2\u00a2\32\3\2\2\2\u00a3\u00a4"+
		"\5c\62\2\u00a4\u00a5\5g\64\2\u00a5\u00a6\5a\61\2\u00a6\u00a7\5]/\2\u00a7"+
		"\u00a8\5m\67\2\u00a8\u00a9\5c\62\2\u00a9\u00aa\5q9\2\u00aa\u00ab\5o8\2"+
		"\u00ab\34\3\2\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7"+
		"w\2\2\u00af\u00b0\7g\2\2\u00b0\36\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3"+
		"\7c\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6"+
		" \3\2\2\2\u00b7\u00b8\5c\62\2\u00b8\u00b9\5_\60\2\u00b9\"\3\2\2\2\u00ba"+
		"\u00bb\5]/\2\u00bb\u00bc\5e\63\2\u00bc\u00bd\5o8\2\u00bd\u00be\5]/\2\u00be"+
		"$\3\2\2\2\u00bf\u00c0\5q9\2\u00c0\u00c1\5a\61\2\u00c1\u00c2\5]/\2\u00c2"+
		"\u00c3\5g\64\2\u00c3&\3\2\2\2\u00c4\u00c5\5_\60\2\u00c5\u00c6\5c\62\2"+
		"\u00c6(\3\2\2\2\u00c7\u00c8\5w<\2\u00c8\u00c9\5a\61\2\u00c9\u00ca\5c\62"+
		"\2\u00ca\u00cb\5e\63\2\u00cb\u00cc\5]/\2\u00cc*\3\2\2\2\u00cd\u00ce\5"+
		"e\63\2\u00ce\u00cf\5i\65\2\u00cf\u00d0\5i\65\2\u00d0\u00d1\5k\66\2\u00d1"+
		",\3\2\2\2\u00d2\u00d3\5k\66\2\u00d3\u00d4\5i\65\2\u00d4\u00d5\5i\65\2"+
		"\u00d5\u00d6\5e\63\2\u00d6.\3\2\2\2\u00d7\u00d8\5e\63\2\u00d8\u00d9\5"+
		"]/\2\u00d9\u00da\5q9\2\u00da\60\3\2\2\2\u00db\u00dc\5c\62\2\u00dc\u00dd"+
		"\5g\64\2\u00dd\62\3\2\2\2\u00de\u00df\5g\64\2\u00df\u00e0\5]/\2\u00e0"+
		"\u00e1\5w<\2\u00e1\64\3\2\2\2\u00e2\u00e3\5c\62\2\u00e3\u00e4\5o8\2\u00e4"+
		"\u00e5\5u;\2\u00e5\u00e6\5i\65\2\u00e6\u00e7\5c\62\2\u00e7\u00e8\5[.\2"+
		"\u00e8\66\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea8\3\2\2\2\u00eb\u00ec\7/\2\2"+
		"\u00ec:\3\2\2\2\u00ed\u00ee\7,\2\2\u00ee<\3\2\2\2\u00ef\u00f0\7\61\2\2"+
		"\u00f0>\3\2\2\2\u00f1\u00f2\7>\2\2\u00f2@\3\2\2\2\u00f3\u00f4\7>\2\2\u00f4"+
		"\u00f5\7?\2\2\u00f5B\3\2\2\2\u00f6\u00f7\7?\2\2\u00f7D\3\2\2\2\u00f8\u00f9"+
		"\5g\64\2\u00f9\u00fa\5i\65\2\u00fa\u00fb\5q9\2\u00fbF\3\2\2\2\u00fc\u0101"+
		"\7$\2\2\u00fd\u0100\5\u0083B\2\u00fe\u0100\n\2\2\2\u00ff\u00fd\3\2\2\2"+
		"\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102"+
		"\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\7$\2\2\u0105"+
		"H\3\2\2\2\u0106\u0108\t\3\2\2\u0107\u0106\3\2\2\2\u0108\u0109\3\2\2\2"+
		"\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010aJ\3\2\2\2\u010b\u010f\t"+
		"\4\2\2\u010c\u010e\t\5\2\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2\u010f"+
		"\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110L\3\2\2\2\u0111\u010f\3\2\2\2"+
		"\u0112\u0116\t\6\2\2\u0113\u0115\t\5\2\2\u0114\u0113\3\2\2\2\u0115\u0118"+
		"\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117N\3\2\2\2\u0118"+
		"\u0116\3\2\2\2\u0119\u011a\7>\2\2\u011a\u011b\7/\2\2\u011bP\3\2\2\2\u011c"+
		"\u011d\7/\2\2\u011d\u011e\7/\2\2\u011e\u0122\3\2\2\2\u011f\u0121\n\7\2"+
		"\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123"+
		"\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0127\7\f\2\2\u0126"+
		"\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\b)"+
		"\2\2\u0129R\3\2\2\2\u012a\u012b\7/\2\2\u012b\u012c\7,\2\2\u012c\u0130"+
		"\3\2\2\2\u012d\u012f\13\2\2\2\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2"+
		"\u0130\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130"+
		"\3\2\2\2\u0133\u0134\7,\2\2\u0134\u0135\7/\2\2\u0135\u0136\3\2\2\2\u0136"+
		"\u0137\b*\2\2\u0137T\3\2\2\2\u0138\u013a\t\b\2\2\u0139\u0138\3\2\2\2\u013a"+
		"\u013b\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2"+
		"\2\2\u013d\u013e\b+\2\2\u013eV\3\2\2\2\u013f\u0140\t\t\2\2\u0140X\3\2"+
		"\2\2\u0141\u0142\t\n\2\2\u0142Z\3\2\2\2\u0143\u0144\t\13\2\2\u0144\\\3"+
		"\2\2\2\u0145\u0146\t\f\2\2\u0146^\3\2\2\2\u0147\u0148\t\r\2\2\u0148`\3"+
		"\2\2\2\u0149\u014a\t\16\2\2\u014ab\3\2\2\2\u014b\u014c\t\17\2\2\u014c"+
		"d\3\2\2\2\u014d\u014e\t\20\2\2\u014ef\3\2\2\2\u014f\u0150\t\21\2\2\u0150"+
		"h\3\2\2\2\u0151\u0152\t\22\2\2\u0152j\3\2\2\2\u0153\u0154\t\23\2\2\u0154"+
		"l\3\2\2\2\u0155\u0156\t\24\2\2\u0156n\3\2\2\2\u0157\u0158\t\25\2\2\u0158"+
		"p\3\2\2\2\u0159\u015a\t\26\2\2\u015ar\3\2\2\2\u015b\u015c\t\27\2\2\u015c"+
		"t\3\2\2\2\u015d\u015e\t\30\2\2\u015ev\3\2\2\2\u015f\u0160\t\31\2\2\u0160"+
		"x\3\2\2\2\u0161\u0162\t\32\2\2\u0162z\3\2\2\2\u0163\u0164\t\33\2\2\u0164"+
		"|\3\2\2\2\u0165\u0166\t\34\2\2\u0166~\3\2\2\2\u0167\u0168\t\35\2\2\u0168"+
		"\u0080\3\2\2\2\u0169\u016a\7w\2\2\u016a\u016b\5\177@\2\u016b\u016c\5\177"+
		"@\2\u016c\u016d\5\177@\2\u016d\u016e\5\177@\2\u016e\u0082\3\2\2\2\u016f"+
		"\u0172\7^\2\2\u0170\u0173\t\36\2\2\u0171\u0173\5\u0081A\2\u0172\u0170"+
		"\3\2\2\2\u0172\u0171\3\2\2\2\u0173\u0084\3\2\2\2\r\2\u00ff\u0101\u0109"+
		"\u010f\u0116\u0122\u0126\u0130\u013b\u0172\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}