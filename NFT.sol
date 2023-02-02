// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TESTMON is ERC721, ERC721Enumerable, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;
    bool public PublicMintIsActive = false;
    bool public WLMintIsActive = false;
    bool public revealed = false;
    mapping(address => bool) public whitelist;
    mapping(address => bool) public walletMints;
    string public baseURI;
    string public notRevealedURI;
    string public baseExtension = ".json";
    uint256 public constant MAX_SUPPLY = 777;
    uint256 public constant PRICE = 0.001 ether;

    constructor() ERC721("TEST", "TEST") {
        // start from 1
        _tokenIdCounter.increment(); 
        
    }
    

    function addToWhitelist(address[] calldata toAddAddresses) external onlyOwner{
        for (uint i = 0; i < toAddAddresses.length; i++) {
            whitelist[toAddAddresses[i]] = true;
        }
    }

    function removeFromWhitelist(address[] calldata toRemoveAddresses) external onlyOwner{
        for (uint i = 0; i < toRemoveAddresses.length; i++) {
            whitelist[toRemoveAddresses[i]] = false;
        }
    }

    function batchMint(uint _batchSize) external onlyOwner{
        for (uint i = 0; i < _batchSize; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(msg.sender, tokenId);
        }
    }

    function safeMint() external payable{
        require(PublicMintIsActive || WLMintIsActive, "Mint is not active");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(walletMints[msg.sender] == false, "You already minted");
        require(msg.value >= PRICE, "You didn't send enough amount");
        if(WLMintIsActive && !PublicMintIsActive){
            require(whitelist[msg.sender] == true, "You are not in Whitelist");
        }
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        walletMints[msg.sender] = true;
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId, uint256 batchSize)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override
        returns (string memory)
    {
        require(
        _exists(tokenId),
        "ERC721Metadata: URI query for nonexistent token"
        );
    
        if(revealed == false) {
            return notRevealedURI;
        }
        string memory currentBaseURI = _baseURI();
        return bytes(currentBaseURI).length > 0
            ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension))
            : "";
   }

    function tokensOfOwner(address _owner) external view returns (uint256[] memory) {
        uint256 tokenCount = balanceOf(_owner);
        uint256[] memory result = new uint256[](tokenCount);
        for (uint256 i = 0; i < tokenCount; i++) {
            result[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return result;
        }


     function startMint() external onlyOwner {
        PublicMintIsActive = true;
    }

    function stopMint() external onlyOwner {
        PublicMintIsActive = false;
    }

    function startWLMint() external onlyOwner{
        WLMintIsActive = true;
    }

    function stopWLMint() external onlyOwner{
        WLMintIsActive = false;
    }

    function reveal() external onlyOwner{
        revealed = true;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    } 

    function setBaseURI(string memory _newBaseURI) public onlyOwner {
        baseURI = _newBaseURI;
    }

    function setNotRevealedURI(string memory _notRevealedURI) public onlyOwner {
        notRevealedURI = _notRevealedURI;
    }

    function withdraw() public payable onlyOwner {
         payable(msg.sender).transfer(address(this).balance);
    }

}